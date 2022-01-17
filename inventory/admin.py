from django.contrib import admin
from .models import Inventory
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(ImportExportModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['title']}),
        ('Merchant',            {'fields': ['merchant']}),
        ('Description',         {'fields': ['description']}),
        ('Specifications',      {'fields': ['specifications']}),
        ('Date Info',           {'fields': ['date']}),
        ('Manufacturer',        {'fields': ['manufacturer']}),
        ('Quantity',            {'fields': ['quantity']}),
    ]
    list_display = ('title', 'merchant', 'description', 'specifications', 'manufacturer', 'quantity', 'date',)
    list_filter = ['merchant', 'title', 'manufacturer']
    search_fields = ['title']