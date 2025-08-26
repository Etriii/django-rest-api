from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # This creates a 'books' endpoint for CRUD operations

urlpatterns = [
    path('api/', include(router.urls)),
]


