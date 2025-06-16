from django.contrib import admin
from .models import Article, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    filter_horizontal = ('user_permissions', 'groups',)
    list_display = ('id', 'username', 'email', 'date_joined', 'is_admin')
    list_display_links = ['id', 'username']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_display_links = ['id', 'title']
    ordering = ['-created_at', 'updated_at']
