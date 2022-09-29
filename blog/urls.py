from django.urls import path
# from .views import 
from . import views
from . views import PostListView


urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', PostListView.as_view(), name='home'),
]
