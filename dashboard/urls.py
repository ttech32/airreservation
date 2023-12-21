from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight, name='flight'),
    path('book/', views.book, name='book'),
    path('<str:pk>', views.control, name='control'),
    path('book/<str:pk>/', views.update_passenger, name='update_passenger'),
    path('delete/<str:pk>/', views.delete_passenger, name='delete_passenger'),
    
]