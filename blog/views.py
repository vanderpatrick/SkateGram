from .models import Post, TutorialPost, Profile, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import PostCreateForm
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


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'detail'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    context_object_name = 'create'
    fields = ['title', 'image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

