from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Vehicle


@admin.register(Vehicle)
class VehiclesAdmin(admin.ModelAdmin):
    list_display = [
        'Regnum',
        'Model',
        'IsRegnumAlien',
        'Created',
        'Updated',
        'is_active',
    ]
    list_filter = [
        'Created',
        'Updated',
        'is_active',
    ]
    search_fields = [
        'Regnum',
        'Model',
    ]
    readonly_fields = [
        'Created',
        'Updated',
    ]
    empty_value_display = EMPTY_VALUE_DISPLAY
