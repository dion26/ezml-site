from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThreadListView.as_view(), name='forum'),

    path('thread/<str:pk>/', views.thread, name='thread'),
    path('create-thread/', views.CreateThreadView.as_view(), name='create-thread'),
    path('update-thread/<str:pk>/', views.UpdateThreadView.as_view(), name='update-thread'),
    path('delete-thread/<str:pk>/', views.deleteThread, name='delete-thread'),

    path('delete-comment/<str:pk>/', views.deleteComment, name='delete-comment'),
    
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),

    path('<str:cat>/', views.OrderedThreadListView.as_view(), name='ordered-forum'),
    path('<str:cat>/<str:ord>/', views.OrderedThreadListView.as_view(), name='ordered-forum')
]