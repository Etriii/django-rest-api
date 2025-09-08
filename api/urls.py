from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import auth_view_set, institute_view_set, program_view_set, school_view_set, user_view_set, system_view_set, user_systems_view_set, student_view_set
from api.serializers.AuthSerializer import CustomTokenObtainPairView


router = DefaultRouter()
router.register(f"profile", auth_view_set.AuthViewSet, basename="profile")
router.register(f"schools", school_view_set.SchoolViewSet, basename="schools")
router.register(f"institutes", institute_view_set.InstituteViewSet, basename="institutes")
router.register(f"programs", program_view_set.ProgramViewSet, basename="programs")
router.register(f"users", user_view_set.UserViewSet, basename="users")
router.register(f"systems", system_view_set.SystemViewSet, basename="systems")
router.register(f"usersystems", user_systems_view_set.UserSystemViewSet, basename="usersystems")
router.register(f"students", student_view_set.StudentViewSet, basename="students")

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
