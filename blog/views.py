from .models import Post, TutorialPost, Profile, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from .forms import (
    UserRegister,
    UpdateUserProfile,
    UserUpadateForm,
    PostForm,
    CommentForm,
)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Create your views here.


def landing(request):
    return render(request, "landing.html")


class PostListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    ordering = ["-created_on"]
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "detail"

    def get_context_data(self, *args, **kwargs):

        context = super(PostDetailView, self).get_context_data()
        total = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = total.total_likes()
        post = Comment.objects.all().order_by("-date")
        context["comments"] = post

        if self.request.user.is_authenticated:
            context["comment_form"] = CommentForm(instance=self.request.user)

        liked = False
        if total.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

    def post(self, request, pk, *args, **kwargs):
        new_comment = Comment(
            content=request.POST.get("content"),
            user=self.request.user,
            post=self.get_object(),
        )
        new_comment.save()
        return HttpResponseRedirect(reverse("detail-post", args=[str(pk)]))


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "create_post.html"
    context_object_name = "create"
    fields = ["title", "image", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_update.html"
    context_object_name = "update"
    fields = ["title", "image", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/home"
    template_name = "post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created!"
            )
            return redirect("login")
    else:
        form = UserRegister()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpadateForm(request.POST, instance=request.user)
        p_form = UpdateUserProfile(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been Updated")
            return redirect("profile")
    else:
        u_form = UserUpadateForm(instance=request.user)
        p_form = UpdateUserProfile(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "profile.html", context)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("detail-post", args=[str(pk)]))


class TutorialListView(ListView):
    model = TutorialPost
    template_name = "tutorials.html"
    context_object_name = "tutorial"
    ordering = ["-created_on"]
    paginate_by = 4


class TutorialDetailView(DetailView):
    model = TutorialPost
    template_name = "tutorial_detail.html"
    context_object_name = "p"
