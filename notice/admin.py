from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', )
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'author__username')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'author')
        }),
        ('Даты', {
            'fields': ('created_at',)
        })
    )