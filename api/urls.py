from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import  TokenRefreshView

from api.views.AuthViewSet import AuthViewSet
from api.serializer.AuthSerializer import CustomTokenObtainPairView

    

router = DefaultRouter()
router.register(f'profile', AuthViewSet, basename='profile')

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
