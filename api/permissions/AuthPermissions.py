from rest_framework.permissions import BasePermission


class ScopedPermission(BasePermission):
    """
    Reusable permission for scoping by related fields.
    
    Usage:
        ScopedPermission(
            school_field="school_id",
            institute_field="institute_id",
            user_field="user_id"
        )
    """

    def __init__(self, school_field=None, institute_field=None, user_field=None):
        self.school_field = school_field
        self.institute_field = institute_field
        self.user_field = user_field
        self.message = "You do not have access to this resource."

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_superuser:
            return True

        if user.is_staff:
            if self.school_field and hasattr(obj, self.school_field) and getattr(user, "school_id", None):
                return getattr(obj, self.school_field) == user.school_id

            if self.institute_field and hasattr(obj, self.institute_field) and getattr(user, "institute_id", None):
                return getattr(obj, self.institute_field) == user.institute_id

        if self.user_field and hasattr(obj, self.user_field):
            return getattr(obj, self.user_field) == user.id

        return False
