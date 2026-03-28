from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from .models import Profile, Category, FoodItem, Order, Favorite
from django.db import models


# --------------------------------------------------------
# 🏠 HOME PAGE (CATEGORIES)
# --------------------------------------------------------
def home_view(request):
    categories = Category.objects.all()
    return render(request, 'food/home.html', {'categories': categories})


# --------------------------------------------------------
# 🔐 AUTHENTICATION
# --------------------------------------------------------
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.profile.role = 'Customer'
            
            if request.FILES.get('profile_image'):
                user.profile.image = request.FILES['profile_image']
            
            user.profile.save()
            user.save()

            messages.success(request, 'Account created! Please log in.')
            return redirect('login')

    return render(request, 'food/user_side/signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.profile.role == 'Admin' or user.is_superuser:
                return redirect('admin-dashboard')
            elif user.profile.role == 'Rider':
                return redirect('rider-dashboard')
            return redirect('user-dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    # Show info message if redirected from a login_required view
    if 'next' in request.GET and not request.method == 'POST':
        messages.info(request, 'Please login first to access the portal.')

    return render(request, 'food/user_side/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# --------------------------------------------------------
# 👤 PROFILE
# --------------------------------------------------------
@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST' and 'update_profile' in request.POST:
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', user.email)
        
        user.first_name = full_name
        user.email = email
        
        if request.FILES.get('profile_image'):
            user.profile.image = request.FILES.get('profile_image')
            user.profile.save()
        
        # Also allow updating username if needed
        username = request.POST.get('username')
        if username and username != user.username:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken!')
            else:
                user.username = username
        
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'food/profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not request.user.check_password(old_password):
            messages.error(request, 'Incorrect current password.')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
        elif len(new_password) < 8:
            messages.error(request, 'Password must be at least 8 characters.')
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password changed successfully!')
            return redirect('profile')
            
    return render(request, 'food/user_side/change_password.html')


# --------------------------------------------------------
# 🍔 FOOD BROWSING
# --------------------------------------------------------
def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = category.items.filter(is_available=True)
    return render(request, 'food/category_items.html', {'category': category, 'items': items})


def food_detail(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, food_item=item).exists()
    return render(request, 'food/food_detail.html', {'item': item, 'is_favorite': is_favorite})


# --------------------------------------------------------
# 🛒 ORDERING
# --------------------------------------------------------
@login_required
def place_order(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        city = request.POST.get('city')
        total_price = item.price * quantity
        
        Order.objects.create(
            user=request.user,
            food_item=item,
            quantity=quantity,
            total_price=total_price,
            city=city,
            status='Pending'
        )
        messages.success(request, 'Order placed successfully! Wait for Admin approval.')
        return redirect('user-dashboard')
    
    cities = ['Bahawalpur', 'Multan', 'Lahore', 'Karachi', 'Islamabad']
    return render(request, 'food/place_order.html', {'item': item, 'cities': cities})


@login_required
def receive_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'On The Way':
        order.status = 'Reached & Received'
        order.save()
        messages.success(request, 'Order marked as Received! Enjoy your meal.')
    return redirect('student-dashboard')


# --------------------------------------------------------
# ❤️ FAVORITES
# --------------------------------------------------------
@login_required
def toggle_favorite(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    fav, created = Favorite.objects.get_or_create(user=request.user, food_item=item)
    if not created:
        fav.delete()
        messages.info(request, f'Removed {item.name} from favorites.')
    else:
        messages.success(request, f'Added {item.name} to favorites.')
    return redirect('food-detail', item_id=item.id)


@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'food/my_favorites.html', {'favorites': favorites})


# --------------------------------------------------------
# 🛡️ ADMIN PANEL
# --------------------------------------------------------
@login_required
def admin_dashboard(request):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
    
    # Get status filter from URL (Default to Pending if not specified)
    status_filter = request.GET.get('status')
    
    # Main orders query
    all_orders = Order.objects.all().order_by('-created_at')
    
    # Apply filter for the table display
    if status_filter:
        if status_filter == 'All':
            orders = all_orders
        else:
            orders = all_orders.filter(status=status_filter)
    else:
        # Default to Pending ONLY for the main table view
        orders = all_orders.filter(status='Pending')
        status_filter = 'Pending'

    categories = Category.objects.all()
    items = FoodItem.objects.all()
    riders = User.objects.filter(profile__role='Rider')
    
    context = {
        'orders': orders,
        'categories': categories,
        'items': items,
        'riders': riders,
        'total_orders_count': all_orders.count(),
        'pending_count': all_orders.filter(status='Pending').count(),
        'active_count': all_orders.filter(status__in=['Preparing', 'On The Way']).count(),
        'delivered_count': all_orders.filter(status='Delivered').count(),
        'rejected_count': all_orders.filter(status='Rejected').count(),
        'current_filter': status_filter
    }
    return render(request, 'food/admin_dashboard.html', context)


@login_required
def update_order_status(request, order_id):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
    
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        rider_id = request.POST.get('rider_id')
        rejection_reason = request.POST.get('rejection_reason')
        
        if new_status:
            order.status = new_status
            if new_status == 'Rejected' and rejection_reason:
                order.rejection_reason = rejection_reason
        
        if rider_id:
            rider = get_object_or_404(User, id=rider_id)
            order.rider = rider
            # Automatically set status to Preparing if a rider is assigned and it was Pending
            if order.status == 'Pending':
                order.status = 'Preparing'
        
        order.save()
        messages.success(request, f'Order #{order.id} updated successfully!')
    return redirect('admin-dashboard')


@login_required
def add_category(request):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        Category.objects.create(name=name, image=image)
        messages.success(request, 'Category added!')
        return redirect('admin-dashboard')
    return render(request, 'food/add_category.html')


@login_required
def add_food_item(request):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
    if request.method == 'POST':
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        category = get_object_or_404(Category, id=category_id)
        FoodItem.objects.create(category=category, name=name, description=description, price=price, image=image)
        messages.success(request, 'Food item added!')
        return redirect('admin-dashboard')
    
    categories = Category.objects.all()
    return render(request, 'food/add_food_item.html', {'categories': categories})


@login_required
def add_rider(request):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone_number')
        image = request.FILES.get('profile_image')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.profile.role = 'Rider'
            if phone:
                user.profile.phone_number = phone
            if image:
                user.profile.image = image
            user.profile.save()
            messages.success(request, f'Rider {username} added successfully!')
    
    return redirect('admin-dashboard')


@login_required
def edit_rider(request, rider_id):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
    
    rider = get_object_or_404(User, id=rider_id, profile__role='Rider')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        password = request.POST.get('password')
        image = request.FILES.get('profile_image')
        
        if User.objects.filter(username=username).exclude(id=rider.id).exists():
            messages.error(request, 'Username already taken!')
        else:
            rider.username = username
            rider.email = email
            rider.profile.phone_number = phone
            if password:
                rider.set_password(password)
            if image:
                rider.profile.image = image
            
            rider.save()
            rider.profile.save()
            messages.success(request, f'Rider {username} updated successfully!')
            return redirect('admin-dashboard')
            
    return render(request, 'food/user_side/edit_rider.html', {'rider': rider})


@login_required
def delete_rider(request, rider_id):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
    
    rider = get_object_or_404(User, id=rider_id, profile__role='Rider')
    username = rider.username
    rider.delete()
    messages.success(request, f'Rider {username} removed successfully.')
    return redirect('admin-dashboard')


# --------------------------------------------------------
# 🚀 USER DASHBOARD (STUDENT DASHBOARD REPURPOSED)
# --------------------------------------------------------
@login_required
def student_dashboard(request):
    status_filter = request.GET.get('status')
    
    # All orders for this user
    all_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    # Apply filter based on status
    if status_filter:
        if status_filter == 'All':
            orders = all_orders
        else:
            orders = all_orders.filter(status=status_filter)
    else:
        # Default view: Shows ONLY pending, preparing, and on the way. Delivered orders are only visible when the Delivered card is clicked.
        orders = all_orders.filter(status__in=['Pending', 'Preparing', 'On The Way'])
        status_filter = 'Active'

    context = {
        'orders': orders,
        'total_orders': all_orders.count(),
        'pending_count': all_orders.filter(status='Pending').count(),
        'preparing_count': all_orders.filter(status='Preparing').count(),
        'ontheway_count': all_orders.filter(status='On The Way').count(),
        'delivered_count': all_orders.filter(status='Delivered').count(),
        'rejected_count': all_orders.filter(status='Rejected').count(),
        'current_filter': status_filter
    }
    
    return render(request, 'food/user_dashboard.html', context)


@login_required
def order_history(request):
    # History: Everything that is NOT Pending
    orders = Order.objects.filter(user=request.user).exclude(status='Pending').order_by('-updated_at')
    
    return render(request, 'food/order_history.html', {'orders': orders})


# --------------------------------------------------------
# 🛵 RIDER PORTAL
# --------------------------------------------------------
@login_required
def rider_dashboard(request):
    if request.user.profile.role != 'Rider':
        return redirect('home')
    
    # Active: Only orders assigned to this rider that are NOT delivered yet
    orders = Order.objects.filter(rider=request.user, status__in=['Preparing', 'On The Way']).order_by('-updated_at')
    
    return render(request, 'food/rider_dashboard.html', {
        'orders': orders
    })


@login_required
def rider_history(request):
    if request.user.profile.role != 'Rider':
        return redirect('home')
    
    # History: Everything else (Delivered, Rejected)
    orders = Order.objects.filter(rider=request.user, status__in=['Delivered', 'Rejected']).order_by('-updated_at')
    
    return render(request, 'food/rider_history.html', {
        'orders': orders
    })


@login_required
def rider_update_status(request, order_id):
    if request.user.profile.role != 'Rider':
        return redirect('home')
    
    order = get_object_or_404(Order, id=order_id, rider=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['On The Way', 'Delivered']:
            order.status = new_status
            order.save()
            messages.success(request, f'Status updated to {new_status}!')
    
    return redirect('rider-dashboard')


@login_required
def confirm_receipt(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice in ['Received', 'Not Received']:
            order.user_confirmation = choice
            order.save()
            
            if choice == 'Received':
                messages.success(request, 'Glad you received your order! Enjoy your meal.')
            else:
                messages.warning(request, 'We are sorry to hear that. Admin has been notified.')
                
    return redirect('user-dashboard')


@login_required
def admin_customer_history(request, user_id):
    if not (request.user.is_superuser or request.user.profile.role == 'Admin'):
        return redirect('home')
        
    customer = get_object_or_404(User, id=user_id)
    orders = Order.objects.filter(user=customer).order_by('-created_at')
    
    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': orders.count(),
        'pending_orders': orders.filter(status='Pending').count(),
        'delivered_orders': orders.filter(status='Delivered', user_confirmation='Received').count(),
        'rejected_orders': orders.filter(status='Rejected').count(),
    }
    
    return render(request, 'food/admin_customer_history.html', context)
