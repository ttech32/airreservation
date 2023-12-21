from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Index, name='index'),
    path('profile/', views.user_profile, name='profile'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('blog/', views.Blog, name='blog'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout_view, name='logout')
]