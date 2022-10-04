from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment
from django.core.exceptions import ValidationError

class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
       username = self.cleaned_data.get('username')
       if User.objects.filter(username=username).exists():
            raise ValidationError("username exists")
       return self.cleaned_data

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data

class UserUpadateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']