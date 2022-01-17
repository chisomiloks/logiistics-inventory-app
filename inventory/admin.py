from django.contrib import admin
from .models import Inventory
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# class InventoryInline(admin.TabularInline):
#     model = Inventory
#     extra = 0


# class InventoryAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,                  {'fields': ['title']}),
    #     ('Merchant',            {'fields': ['merchant']}),
    #     ('Description',         {'fields': ['description']}),
    #     ('Specifications',      {'fields': ['specifications']}),
    #     ('Date Info',           {'fields': ['date']}),
    #     ('Manufacturer',        {'fields': ['manufacturer']}),
    #     ('Quantity',            {'fields': ['quantity']}),
    # ]
    # # inlines = [InventoryInline,]
    # list_display = ('title', 'merchant', 'description', 'specifications', 'manufacturer', 'quantity', 'date',)
    # list_filter = ['merchant']
    # search_fields = ['title']

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
    # inlines = [InventoryInline,]
    list_display = ('title', 'merchant', 'description', 'specifications', 'manufacturer', 'quantity', 'date',)
    list_filter = ['merchant']
    search_fields = ['title']