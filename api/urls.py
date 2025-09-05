from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import AuthViewSet, InstituteView, SchoolView, ProgramView
from api.serializers.AuthSerializer import CustomTokenObtainPairView


router = DefaultRouter()
router.register(f"profile", AuthViewSet.AuthViewSet, basename="profile")
router.register(f"schools", SchoolView.SchoolViewSet, basename="schools")
router.register(f"institutes", InstituteView.InstituteViewSet, basename="institutes")
router.register(f"programs", ProgramView.ProgramViewSet, basename="programs")


urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
