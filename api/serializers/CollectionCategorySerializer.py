from rest_framework import serializers
from api.models import CollectionCategory
from api.serializers import InstituteSerializers


class CollectionCategoryReadSerializer(serializers.ModelSerializer):
    institute = InstituteSerializers.InstituteReadSerializer()

    class Meta:
        model = CollectionCategory
        fields = "__all__"


class CollectionCategoryReadSlimSerializer(serializers.ModelSerializer):
    institute = InstituteSerializers.InstituteReadSlimSerializer()

    class Meta:
        model = CollectionCategory
        fields = ["id", "category_name", "collection_fee", "description", "institute"]
        read_only_fields = fields


class CollectionCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCategory
        fields = ["category_name", "collection_fee", "description", "institute"]


class CollectionCategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCategory
        fields = ["id", "category_name"]
