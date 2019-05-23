from django.urls import path
from . import views

urlpatterns = [
    path('myposts/', views.myPosts, name='myposts'),
    path('myposts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('like/', views.like_post, name='like_post'),

]
