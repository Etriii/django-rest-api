from rest_framework import serializers, validators

from api.models import UserSystem

from .UserSerializers import UserReadSlimSerializer
from .SystemSerializers import SystemReadSlimSerializer


class UserSystemReadSerializer(serializers.ModelSerializer):
    # user = UserReadSlimSerializer()
    # system = serializers.CharField(source="system.name", read_only=True)

    # class Meta:
    #     model = UserSystem
    #     fields = "__all__"
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    institute = serializers.CharField(
        source="user.institute.institute_name", read_only=True, default=None
    )

    system = serializers.CharField(source="system.name", read_only=True)

    class Meta:
        model = UserSystem
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "institute",
            "system",
        ]


class UserSystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSystem
        fields = ["user", "system"]
        read_only_fields = ["id", "created_at", "updated_at"]


class UserSystemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSystem
        fields = ["user", "system"]

        validators = [
            validators.UniqueTogetherValidator(
                queryset=UserSystem.objects.all(),
                fields=["user", "system"],
                message="This user is already linked to this system.",
            )
        ]


class UserSysemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSystem
        fields = ["user", "system"]
        
        validators = [
            validators.UniqueTogetherValidator(
                queryset=UserSystem.objects.all(),
                fields=["user", "system"],
                message="This user is already linked to this system.",
            )
        ]
