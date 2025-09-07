from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import System
from api.serializers.SystemSerializers import SystemSerializer
from api.utils.custom_paginations import CustomPagination


from drf_spectacular.utils import extend_schema
@extend_schema(tags=["System"])

class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all().order_by("id")
    pagination_class = CustomPagination # list actions use this
    permission_classes = [IsAuthenticated]
    serializer_class = SystemSerializer    

