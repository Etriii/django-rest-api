from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # token["permissions"] = list(user.get_all_permissions())
        token["groups"] = list(user.groups.values_list("name", flat=True))

        institute_data = {"id": None, "name": None}
        school_data = {"id": None, "name": None}

        if hasattr(user, "institute") and user.institute:
            institute_data = {
                "id": getattr(user.institute, "id", None),
                "name": getattr(user.institute, "institute_name", None),
            }
            school_data = {
                "id": getattr(user.institute.school, "id", None),
                "name": getattr(user.institute.school, "school_name", None),
            }

        token["institute"] = institute_data
        token["school"] = school_data

        systems = getattr(user, "user_systems", None)
        system_list = []
        if systems:
            system_list = [
                {
                    "id": getattr(us.system, "id", None),
                    "name": getattr(us.system, "name", None),
                }
                for us in systems.select_related("system").all()
            ]
        token["systems"] = system_list

        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
