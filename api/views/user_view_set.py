from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import User
from api.serializers.UserSerializers import UserCreateSerializer, UserReadSerializer, UserUpdateSerializer, UserDeleteSerializer
from api.utils.custom_paginations import CustomPagination


from drf_spectacular.utils import extend_schema
@extend_schema(tags=["User"])

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    pagination_class = CustomPagination # list actions use this
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        elif self.action == "retrieve":
            return UserReadSerializer
        elif self.action in ["update", "partial_update"]:
            return UserUpdateSerializer
        elif self.action == "destroy":
            return UserDeleteSerializer
        return UserReadSerializer

