from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Colors


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    """ Цвета - Администрирование """
    fields = []
    list_display = ['name', 'is_active']
    empty_value_display = EMPTY_VALUE_DISPLAY