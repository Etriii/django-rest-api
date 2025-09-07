from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import School
from api.serializers.SchoolSerializers import SchoolCreateSerializer,SchoolReadSerializer,SchoolUpdateSerializer,SchoolDeleteSerializer
from api.utils.custom_paginations import CustomPagination


from drf_spectacular.utils import extend_schema
@extend_schema(tags=["School"])

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by("school_name")
    pagination_class = CustomPagination # list actions use this
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == "create":
            return SchoolCreateSerializer
        elif self.action == "retrieve":
            return SchoolReadSerializer
        elif self.action in ["update", "partial_update"]:
            return SchoolUpdateSerializer
        elif self.action == "destroy":
            return SchoolDeleteSerializer
        return SchoolReadSerializer

