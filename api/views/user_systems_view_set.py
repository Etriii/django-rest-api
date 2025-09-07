from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import UserSystem
from api.serializers.UserSystemSerializers import (
    UserSystemReadSerializer,
    UserSystemSerializer,
    UserSystemCreateSerializer,
    UserSysemUpdateSerializer,
)
from api.utils.custom_paginations import CustomPagination

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["User System"])
class UserSystemViewSet(viewsets.ModelViewSet):
    queryset = UserSystem.objects.all().order_by("id")
    pagination_class = CustomPagination  # list actions use this
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return UserSystemCreateSerializer
        elif self.action == "retrieve":
            return UserSystemReadSerializer

        elif self.action in ["update", "partial_update"]:
            return UserSysemUpdateSerializer
        elif self.action == "destroy":
            return UserSystemSerializer
        return UserSystemReadSerializer
