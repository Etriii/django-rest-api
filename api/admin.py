from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from .models import User, School, System, UserSystem, Institute, Program, Student, CollectionCategory, Fee, AttendanceEvent, AttendanceRecord, EventSetting, Payment, PaymentSubmission
#GroupProfile

# Custom User admin
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Institute Info", {"fields": ("institute",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Institute Info", {"fields": ("institute",)}),
    )

    list_display = ("username", "email", "institute", "is_staff", "is_active")
    search_fields = ("username", "email", "institute")
    
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

admin.site.register(School)
admin.site.register(System)
admin.site.register(UserSystem)
admin.site.register(Institute)
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(CollectionCategory)
admin.site.register(Fee)
admin.site.register(AttendanceEvent)
admin.site.register(AttendanceRecord)
admin.site.register(EventSetting)
admin.site.register(Payment)
admin.site.register(PaymentSubmission)
