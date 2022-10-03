from django.contrib import admin

from .models import Post, Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'comment_author',
        'comment',
        'date_added',
    )

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'updated_on',
        'content',
        'author',
        'created_on',


    )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)



