from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import auth_view_set, institute_view_set, program_view_set, school_view_set, user_view_set
from api.serializers.AuthSerializer import CustomTokenObtainPairView


router = DefaultRouter()
router.register(f"profile", auth_view_set.AuthViewSet, basename="profile")
router.register(f"schools", school_view_set.SchoolViewSet, basename="schools")
router.register(f"institutes", institute_view_set.InstituteViewSet, basename="institutes")
router.register(f"programs", program_view_set.ProgramViewSet, basename="programs")
router.register(f"users", user_view_set.UserViewSet, basename="users")


urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
