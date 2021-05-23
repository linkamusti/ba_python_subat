from django.contrib import admin


from .models import Blog, Comment

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('text', 'title', 'author', 'publish_date', 'avg_rating')
    list_filter = ('author',)
    search_fields = ('title', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'username', 'rating', 'blog')
    list_filter = ('username', 'blog')
    search_fields = ('username', 'blog')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)