from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'create_date', 'image', 'is_published', 'slug')
    list_filter = ('create_date', 'is_published')
