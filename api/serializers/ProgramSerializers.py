from rest_framework import serializers
from api.models import Program
from api.serializers.InstituteSerializers import (
    InstituteReadSerializer,
    InstituteReadSlimSerializer,
)


class ProgramCreateSerializer(serializers.ModelSerializer):
    """Schema for creating a program"""

    class Meta:
        model = Program
        fields = ["name", "status", "institute"]


class ProgramReadSerializer(serializers.ModelSerializer):
    """Detailed schema for reading/retrieving"""

    institute = InstituteReadSerializer()

    class Meta:
        model = Program
        fields = [
            "id",
            "name",
            "status",
            "institute",
            "created_at",
            "updated_at",
            "updated_by",
        ]


class ProgramSlimReadSerializer(serializers.ModelSerializer):
    institute = InstituteReadSlimSerializer(read_only=True)

    class Meta:
        model = Program
        fields = ["id", "name", "status", "institute"]

        read_only_fields = fields


class ProgramUpdateSerializer(serializers.ModelSerializer):
    """Schema for updates"""

    class Meta:
        model = Program
        fields = ["name", "status", "institute"]


class ProgramDeleteSerializer(serializers.ModelSerializer):
    """Schema for confirming deletion"""

    class Meta:
        model = Program
        fields = ["id", "name"]
