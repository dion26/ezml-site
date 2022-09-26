from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name='update-user'),
    path('', views.home, name='home'),
]