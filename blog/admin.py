from django.contrib import admin

from blog.models import Tag, Post

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('summary', 'content')

admin.site.register(Post, PostAdmin)