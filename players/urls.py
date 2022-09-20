from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/<slug:slug>/', views.PlayerDetailView.as_view(), name='player-detail'),
    
    path('<str:pk>/', views.PlayerDetailAPIView.as_view())
    
]