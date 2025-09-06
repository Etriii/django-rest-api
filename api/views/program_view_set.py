from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Program
from api.serializers.ProgramSerializers import (
    ProgramCreateSerializer,
    ProgramReadSerializer,
    ProgramUpdateSerializer,
    ProgramDeleteSerializer,
)
from api.utils.custom_paginations import CustomPagination


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all().order_by("name")
    pagination_class = CustomPagination  # list actions use this
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return ProgramCreateSerializer
        elif self.action == "retrieve":
            return ProgramReadSerializer
        elif self.action in ["update", "partial_update"]:
            return ProgramUpdateSerializer
        elif self.action == "destroy":
            return ProgramDeleteSerializer
        return ProgramReadSerializer
