from django.urls import path
from . import views

urlpatterns = [
    # path('<str:pk>/<slug:slug>/', views.PlayerDetailView.as_view(), name='player-detail'),
    path('', views.PlayerListApiView.as_view()),
    path('create/', views.PlayerCreateAPIView.as_view()),
    path('social/', views.SocialListApiView.as_view()),
    path('social/create/', views.SocialCreateAPIView.as_view()),
    path('social/<str:pk>/', views.SocialDetailAPIView.as_view()),
    path('<str:public_id>/<slug:slug>/', views.PlayerDetailAPIView.as_view()),
    path('<str:public_id>/<slug:slug>/update/', views.PlayerUpdateAPIView.as_view()),
    path('<str:public_id>/<slug:slug>/delete/', views.PlayerDeleteAPIView.as_view()),
]