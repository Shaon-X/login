from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name="login_url"),
    path('home/', views.home_page, name="home_url"),
    path('logout_page/', views.logout_page, name="logout_url"),
    path('register_page/', views.register_page, name="register_url"),
    path('profile_page/', views.profile_page, name="profile_url"),
    path('delete_page/', views.delete_page, name="delete_url"),
    path('admin/', views.admin_page, name='admin_url'),
]
