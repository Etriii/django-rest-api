from rest_framework.permissions import BasePermission

class CanCreateSchool(BasePermission):
    message = "Only staff users can create schools."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class CanUpdateSchool(BasePermission):
    message = "You do not have permission to update schools."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_perm("app.change_school")


class CanDeleteSchool(BasePermission):
    message = "Only superusers can delete schools."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser
