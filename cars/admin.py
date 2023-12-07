from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Vehicle


@admin.register(Vehicle)
class VehiclesAdmin(admin.ModelAdmin):
    """ Транспортные средства - Администрирование """
    list_display = [
        'regnum',
        'model',
        'is_alien',
        'created',
        'updated',
        'is_active',
    ]
    list_filter = [
        'created',
        'updated',
        'is_active',
    ]
    search_fields = [
        'regnum',
        'model',
    ]
    readonly_fields = [
        'created',
        'updated',
    ]
    empty_value_display = EMPTY_VALUE_DISPLAY
