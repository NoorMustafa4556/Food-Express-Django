from django.contrib import admin
from .models import Profile, Category, FoodItem, Order, Favorite

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available']
    list_filter = ['category', 'is_available']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'food_item', 'quantity', 'total_price', 'status', 'created_at']
    list_filter = ['status', 'city', 'created_at']
    search_fields = ['user__username', 'food_item__name']

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'food_item', 'created_at']