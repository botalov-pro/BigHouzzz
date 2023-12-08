from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Vehicle, VehicleCategory


class DriverAdminInline(admin.TabularInline):
    model = Vehicle.drivers.through
    verbose_name = 'Водитель'
    verbose_name_plural = 'Водители'
    extra = 0  # Количество дополнительных пустых строк в форме
    classes = ['collapse']


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    """ Категории транспортных средств - Администрирование """
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
            'Водители',
            {
                "classes": ['collapse'],
                "fields": [
                    'drivers',
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
        'category',
        'is_active',
    ]
    list_filter = [
        'category',
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
    ordering = [
        'regnum',
    ]
    filter_horizontal = [
        'drivers',
    ]
    inlines = (DriverAdminInline, )
    model = Vehicle
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(VehiclesAdmin, self).get_inline_instances(request, obj)

