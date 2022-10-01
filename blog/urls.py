from django.urls import path
# from .views import 
from . import views
from . views import PostListView, PostDetailView, CreatePostView, EditPostView, DeletePostView, LikeView



urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail-post'),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
