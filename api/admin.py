# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from .models import User #GroupProfile

# Custom User admin
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Institute Info", {"fields": ("institute_id",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Institute Info", {"fields": ("institute_id",)}),
    )

    list_display = ("username", "email", "institute_id", "is_staff", "is_active")
    search_fields = ("username", "email", "institute_id")

# # Group admin with profile inline
# class GroupProfileInline(admin.StackedInline):
#     model = GroupProfile
#     can_delete = False
#     verbose_name_plural = "Profile"

# admin.site.unregister(Group)

# @admin.register(Group)
# class CustomGroupAdmin(GroupAdmin):
#     inlines = (GroupProfileInline,)
#     list_display = ("name", "get_system_id")

#     def get_system_id(self, obj):
#         return obj.profile.system_id if hasattr(obj, "profile") else "-"
#     get_system_id.short_description = "System ID"
