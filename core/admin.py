from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Colors, Review


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    """ Цвета - Администрирование """
    fields = []
    list_display = ['id', 'name', 'is_active']
    list_display_links = ['name',]
    list_filter = ['is_active',]
    search_fields = ['name',]
    ordering = ['name',]
    empty_value_display = EMPTY_VALUE_DISPLAY

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Отзывы - Администрирование """
    fields = [
        'user',
        'rating',
        'text',
        'is_active',
        'created',
    ]
    list_display = ['id', 'user', 'text', 'rating', 'created', 'is_active',]
    list_display_links = ['id',]
    list_filter = ['is_active', 'created', 'rating',]
    readonly_fields = [
        'created',
    ]
    search_fields = ['text',]
    ordering = ['-created',]
    empty_value_display = EMPTY_VALUE_DISPLAY
