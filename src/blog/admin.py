from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Tag,PostFeaturedImage

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(PostFeaturedImage)
