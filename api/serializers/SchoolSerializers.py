from rest_framework import serializers
from api.models import School

class SchoolCreateSerializer(serializers.ModelSerializer):
    """Schema for creating a school"""

    class Meta:
        model = School
        fields = ["school_name", "logo", "location"]


class SchoolReadSerializer(serializers.ModelSerializer):
    """Detailed schema for reading/retrieving"""

    class Meta:
        model = School
        fields = [
            "id",
            "school_name",
            "logo",
            "location",
            "created_at",
            "updated_at",
            "updated_by",
        ]


class SchoolUpdateSerializer(serializers.ModelSerializer):
    """Schema for updates"""

    class Meta:
        model = School
        fields = ["school_name", "logo", "location"]


class SchoolDeleteSerializer(serializers.ModelSerializer):
    """Schema for confirming deletion"""

    class Meta:
        model = School
        fields = ["id", "school_name"]