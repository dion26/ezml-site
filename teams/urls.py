from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeamListApiView.as_view()),
    path('create/', views.TeamCreateAPIView.as_view()),
    path('membership/', views.MembershipListApiView.as_view()),
    path('membership/create/', views.MembershipCreateApiView.as_view()),
]