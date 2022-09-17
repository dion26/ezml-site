from django.urls import path
from . import views

urlpatterns = [
    path('', views.MatchesView.as_view(), name='matches')
]