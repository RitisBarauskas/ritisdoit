from django.contrib import admin

from .models import Category, Article
from .enums import ArticleStatus


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'type', 'status')
    search_fields = ('title', 'author__username')
    list_filter = ('type', 'status', 'categories')
    date_hierarchy = 'published_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'categories')
        }),
        ('Дополнительно', {
            'fields': ('published_at', 'type', 'status')
        }),
    )
    filter_horizontal = ('categories',)
    actions = ['make_published', 'make_draft', 'make_archived']

    def make_published(self, request, queryset):
        queryset.update(status=ArticleStatus.PUBLISHED)

    make_published.short_description = 'Опубликовать'

    def make_draft(self, request, queryset):
        queryset.update(status=ArticleStatus.DRAFT)

    make_draft.short_description = 'Снять с публикации'

    def make_archived(self, request, queryset):
        queryset.update(status=ArticleStatus.ARCHIVED)

    make_archived.short_description = 'Архивировать'
