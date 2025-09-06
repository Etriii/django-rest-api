from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import System
from api.serializers.SystemsSerializers import SystemSerializer
from api.utils.custom_paginations import CustomPagination


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all().order_by("id")
    serializer_class = SystemSerializer
    pagination_class = CustomPagination 
    permission_classes = [IsAuthenticated]
