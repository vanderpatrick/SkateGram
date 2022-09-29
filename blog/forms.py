from django import forms
from .models import Post
from cloudinary.models import CloudinaryField



class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"