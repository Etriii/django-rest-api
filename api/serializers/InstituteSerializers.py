from rest_framework import serializers
from api.models import Institute
from api.serializers.SchoolSerializers import SchoolReadSerializer


class InstituteCreateSerializer(serializers.ModelSerializer):
    """Schema for creating an institute"""

    class Meta:
        model = Institute
        fields = ["institute_name", "logo", "school"]


class InstituteReadSerializer(serializers.ModelSerializer):
    """Detailed schema for reading/retrieving"""
    
    class Meta:
        model = Institute
        fields = [
            "id",
            "institute_name",
            "logo",
            "school",
            "created_at",
            "updated_at",
            "updated_by",
        ]
        
class InstituteReadSlimSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField(source="school.id", read_only=True)
    school_name = serializers.CharField(source="school.school_name", read_only=True)
    
    class Meta:
        model = Institute
        fields = ["id", "institute_name", "school_id", "school_name"]


class InstituteUpdateSerializer(serializers.ModelSerializer):
    """Schema for updates"""

    class Meta:
        model = Institute
        fields = ["institute_name", "logo", "school"]


class InstituteDeleteSerializer(serializers.ModelSerializer):
    """Schema for confirming deletion"""

    class Meta:
        model = Institute
        fields = ["id", "institute_name"]
