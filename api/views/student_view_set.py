from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from api.models import Student
from api.serializers.StudentSerializers import (
    StudentReadSlimSerializer,
    StudentSerializer,
)
from api.utils.custom_paginations import CustomPagination

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Student"])
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("id")
    pagination_class = CustomPagination  # list actions use this
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return StudentSerializer
        elif self.action == "retrieve":
            return StudentReadSlimSerializer
        elif self.action in ["update", "partial_update"]:
            return StudentSerializer
        elif self.action == "destroy":
            return StudentSerializer
        return StudentReadSlimSerializer
