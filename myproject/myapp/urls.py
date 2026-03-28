from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ------------------------
    # HOME + AUTH ROUTES
    # ------------------------
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ------------------------
    # PROFILE ROUTE
    # ------------------------
    path('profile/', views.profile_view, name='profile'),
    path('profile/change-password/', views.change_password, name='change-password'),

    # ------------------------
    # FOOD BROWSING ROUTES
    # ------------------------
    path('category/<int:category_id>/', views.category_items, name='category-items'),
    path('food/<int:item_id>/', views.food_detail, name='food-detail'),
    path('favorites/toggle/<int:item_id>/', views.toggle_favorite, name='toggle-favorite'),
    path('favorites/', views.my_favorites, name='my-favorites'),

    # ------------------------
    # STUDENT / CUSTOMER ROUTES
    # ------------------------
    path('dashboard/', views.student_dashboard, name='user-dashboard'),
    path('history/', views.order_history, name='order-history'),
    path('order/<int:item_id>/place/', views.place_order, name='place-order'),
    path('order/<int:order_id>/receive/', views.receive_order, name='receive-order'),
    path('order/<int:order_id>/confirm-receipt/', views.confirm_receipt, name='confirm-receipt'),

    # ------------------------
    # ADMIN ROUTES
    # ------------------------
    path('admin-panel/', views.admin_dashboard, name='admin-dashboard'),
    path('admin-panel/category/add/', views.add_category, name='add-category'),
    path('admin-panel/food/add/', views.add_food_item, name='add-food-item'),
    path('admin-panel/riders/add/', views.add_rider, name='add-rider'),
    path('admin-panel/riders/edit/<int:rider_id>/', views.edit_rider, name='edit-rider'),
    path('admin-panel/riders/delete/<int:rider_id>/', views.delete_rider, name='delete-rider'),
    path('order/<int:order_id>/update-status/', views.update_order_status, name='update-order-status'),
    path('admin-panel/customer/<int:user_id>/', views.admin_customer_history, name='admin-customer-history'),

    # ------------------------
    # RIDER ROUTES
    # ------------------------
    path('rider/', views.rider_dashboard, name='rider-home'), # Redirect/Alias to dashboard
    path('rider/dashboard/', views.rider_dashboard, name='rider-dashboard'),
    path('rider/history/', views.rider_history, name='rider-history'),
    path('rider/order/<int:order_id>/update-status/', views.rider_update_status, name='rider-update-status'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
