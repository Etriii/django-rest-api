from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Institute
from api.serializers.InstituteSerializers import (
    InstituteCreateSerializer,
    InstituteReadSerializer,
    InstituteUpdateSerializer,
    InstituteDeleteSerializer,
)
from api.utils.custom_paginations import CustomPagination


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all().order_by("institute_name")
    pagination_class = CustomPagination  # list actions use this
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return InstituteCreateSerializer
        elif self.action == "retrieve":
            return InstituteReadSerializer
        elif self.action in ["update", "partial_update"]:
            return InstituteUpdateSerializer
        elif self.action == "destroy":
            return InstituteDeleteSerializer
        return InstituteReadSerializer
