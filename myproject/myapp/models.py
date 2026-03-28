from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# -----------------------------------------
# 1. PROFILE MODEL
# -----------------------------------------
class Profile(models.Model):
    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('Admin', 'Admin'),
        ('Rider', 'Rider'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Customer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


# -----------------------------------------
# 2. FOOD CATEGORY MODEL
# -----------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_pics/', blank=True, null=True)

    def __str__(self):
        return self.name


# -----------------------------------------
# 3. FOOD ITEM MODEL
# -----------------------------------------
class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food_items/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# -----------------------------------------
# 4. ORDER MODEL
# -----------------------------------------
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
        ('Rejected', 'Rejected'),
    ]

    CITY_CHOICES = [
        ('Bahawalpur', 'Bahawalpur'),
        ('Multan', 'Multan'),
        ('Lahore', 'Lahore'),
        ('Karachi', 'Karachi'),
        ('Islamabad', 'Islamabad'),
    ]

    USER_CONFIRMATION_CHOICES = [
        ('Pending', 'Waiting for User Feedback'),
        ('Received', 'Yes, Received'),
        ('Not Received', 'No, Didn\'t Receive'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50, choices=CITY_CHOICES, default='Bahawalpur')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    user_confirmation = models.CharField(max_length=20, choices=USER_CONFIRMATION_CHOICES, default='Pending')
    rejection_reason = models.TextField(blank=True, null=True)
    rider = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# -----------------------------------------
# 5. FAVORITE MODEL
# -----------------------------------------
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'food_item')

    def __str__(self):
        return f"{self.user.username} - {self.food_item.name}"


# -----------------------------------------
# 6. AUTO CREATE & SAVE PROFILE SIGNALS
# -----------------------------------------
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

