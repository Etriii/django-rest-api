from .auth_view_set import AuthViewSet
from .institute_view_set import InstituteViewSet
from .program_view_set import ProgramViewSet
from .school_view_set import SchoolViewSet
from .user_view_set import UserViewSet
from .system_view_set import SystemViewSet
from .user_systems_view_set import UserSystemViewSet
from .student_view_set import StudentViewSet
from .collection_category_view_set import CollectionCategoryViewSet

__all__  = [
    "AuthViewSet",
    "InstituteViewSet",
    "ProgramViewSet",
    "SchoolViewSet",
    "UserViewSet",
    "SystemViewSet",
    "UserSystemViewSet",
    "StudentViewSet",
    "CollectionCategoryViewSet",
]