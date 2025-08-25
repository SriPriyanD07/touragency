from django.urls import path
from django.contrib import admin
from . import views

app_name = 'tours'  # Add app namespace

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # Contact pages
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_sucess_view, name='contact-success'),  # Fixed typo in path
    
    # Data pages
    path('data/', views.data_views, name='data'),
    path('hot-deals/', views.hot_deals_view, name='hot-deals'),
    
    # Cost tier pages
    path('cost/select/<int:tour_id>/', views.cost_tier_select_view, name='cost-tier-select'),
    path('cost/detail/<int:tour_id>/<str:tier>/', views.cost_tier_detail_view, name='cost-tier-detail'),
    
    # Auth-related URLs (consider moving these to auth1_app/urls.py in the future)
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='login-redirect'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Protected views
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]
