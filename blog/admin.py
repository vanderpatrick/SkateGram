from django.contrib import admin
from .models import Post, Comment, TutorialPost, Profile
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(TutorialPost)
admin.site.register(Profile)
