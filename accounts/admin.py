from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser



# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'email', 'username', 'company', 'date_joined',]
    list_filter = ['company']
    search_fields = ['username', 'company']
    fieldsets = UserAdmin.fieldsets + (
        ( None,     {'fields': ('company',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,      {'fields': ('company',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)