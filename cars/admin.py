from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Vehicle, VehicleCategory


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_active',
    ]
    list_filter = [
        'is_active',
    ]
    search_fields = [
        'name',
    ]
    empty_value_display = EMPTY_VALUE_DISPLAY

@admin.register(Vehicle)
class VehiclesAdmin(admin.ModelAdmin):
    """ Транспортные средства - Администрирование """
    fieldsets = [
        (
            None,
            {
                'fields': [
                    ('regnum', 'is_alien'),
                    'category',
                    'model',
                    'color',
                    'is_active',
                ],
            },
        ),
        (
            'Дополнительно',
            {
                "classes": ['collapse'],
                "fields": [
                    ('updated', 'created'),
                ],
            },
        ),
    ]
    list_display = [
        'regnum',
        'model',
        'created',
        'updated',
        'is_active',
    ]
    list_filter = [
        'model',
        'color',
        'created',
        'updated',
        'is_active',
        'is_alien',
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
