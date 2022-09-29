from .models import Post, TutorialPost, Profile, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
# from .forms import UserRegister, UpdateUserProfile, UserUpadateForm, PostForm
from tinymce import models as tinymce_models
# Create your views here.


def landing(request):
    return render(request, 'landing.html')

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_on']
    paginate_by = 4