from django.contrib import admin
from django.utils.safestring import mark_safe
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Vehicle, VehicleCategory


#class DriverAdminInline(admin.TabularInline):
#    model = Vehicle.drivers.through
#    verbose_name = 'Водитель'
#    verbose_name_plural = 'Водители'
#    extra = 0  # Количество дополнительных пустых строк в форме
#    classes = ['collapse']


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
                    ('vehicle_image', 'main_image'),
                ],
            },
        ),
        (
            'Водители',
            {
                "classes": ['collapse'],
                "fields": [
                    'driver',
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
        'vehicle_image',
        'regnum',
        'model',
        'created',
        'updated',
        'category',
        'is_active',
    ]
    list_display_links = ['regnum', ]
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
        'vehicle_image',
        'created',
        'updated',
    ]
    ordering = [
        'regnum',
    ]
#    filter_horizontal = [
#        'driver',
#    ]
#    inlines = (DriverAdminInline, )
#    model = Vehicle
    empty_value_display = EMPTY_VALUE_DISPLAY

    def vehicle_image(self, obj):
        """ Возвращаем изображение для миниатюры ТС """
        if obj.main_image:
            return mark_safe(
                f'<img src="{obj.main_image.url}" alt="" height="50px">')
        else:
            return mark_safe(f'<img src="" alt="">')

    # Переназываем поле для изображения миниатюры ТС
    vehicle_image.short_description = 'Миниатюра'
