from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Regnum', 'Model', 'IsRegnumAlien', 'Created', 'Updated']
    list_filter = ['Created', 'Updated']