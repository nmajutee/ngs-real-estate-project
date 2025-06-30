from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AgentProfile

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AgentProfile)