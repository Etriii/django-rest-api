from .auth_permission import ScopedPermission
from .school_permissions import CanCreateSchool, CanDeleteSchool, CanUpdateSchool

__all__ = ["ScopedPermission", "CanCreateSchool", "CanDeleteSchool", "CanUpdateSchool"]
