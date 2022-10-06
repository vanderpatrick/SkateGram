from django.contrib import admin
from .models import Post, Comment, TeamPost, Profile
# Register your models here.


# Admin registration of Models


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(TeamPost)
admin.site.register(Profile)
