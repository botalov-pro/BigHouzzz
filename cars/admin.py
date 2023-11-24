from django.contrib import admin
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from .models import Vehicle


@admin.register(Vehicle)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Regnum', 'Model', 'IsRegnumAlien', 'Created', 'Updated']
    list_filter = ['Created', 'Updated']
    empty_value_display = EMPTY_VALUE_DISPLAY
