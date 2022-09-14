from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/<str:nick/', views.PlayerDetailView.as_view(), name='player-detail')
]