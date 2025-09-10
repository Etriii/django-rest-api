from rest_framework import serializers
from api.models import User
from api.serializers.InstituteSerializers import InstituteReadSlimSerializer

class UserCreateSerializer(serializers.ModelSerializer):
    """Schema for creating a user"""

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "status",
            "institute",
        ]
        extra_kwargs = {
            "password": {"write_only": True},  
        }

    def create(self, validated_data):
        """Use Django's built-in user creation (handles password hashing)"""
        password = validated_data.pop("password", None)
        user = User.objects.create_user(password=password, **validated_data)
        return user

class UserReadSerializer(serializers.ModelSerializer):
    """Detailed schema for reading/retrieving"""

    institute =  InstituteReadSlimSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "status",
            "institute",
            "is_superuser",
            "is_staff",
            "is_active",
            "created_at",
            "updated_at",
            "updated_by",
        ]
        read_only_fields = fields
        
class UserReadSlimSerializer(serializers.ModelSerializer):
    """Short schema for reading/retrieving"""

    institute =  InstituteReadSlimSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            "username",
            "email",
            "first_name",
            "last_name",
            "institute",
        ]
        read_only_fields = fields


class UserUpdateSerializer(serializers.ModelSerializer):
    """Schema for updates"""

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "status",
            "institute",
            "is_active",
        ]


class UserDeleteSerializer(serializers.ModelSerializer):
    """Schema for confirming deletion"""

    class Meta:
        model = User
        fields = ["id", "username", "email"]
