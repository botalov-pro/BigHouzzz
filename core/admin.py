from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Colors


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
