from django.contrib import admin
from .models import Inventory
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(Inventory)