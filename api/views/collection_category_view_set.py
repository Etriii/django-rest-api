from api.models import CollectionCategory
from api.serializers.CollectionCategorySerializer import (
    CollectionCategoryReadSerializer,
    CollectionCategoryReadSlimSerializer,
    CollectionCategoryCreateSerializer,
    CollectionCategoryDeleteSerializer,
)
from rest_framework import viewsets
from api.utils.custom_paginations import CustomPagination
from rest_framework.permissions import IsAuthenticated


from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Collection Category"])
class CollectionCategoryViewSet(viewsets.ModelViewSet):
    queryset = CollectionCategory.objects.all().order_by("id")
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return CollectionCategoryCreateSerializer
        elif self.action == "retrieve":
            return CollectionCategoryReadSerializer
        elif self.action in ["update", "partial_update"]:
            return CollectionCategoryCreateSerializer
        elif self.action == "destroy":
            return CollectionCategoryDeleteSerializer
        return CollectionCategoryReadSlimSerializer
