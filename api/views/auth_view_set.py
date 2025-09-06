from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import AuthUserSerializer
from api.utils.token_extractor import get_user_from_token


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AuthUserSerializer

    def list(self, request):
        user, exp, groups = get_user_from_token(request)  # , groups, permissions

        if not user:
            return Response({"error": "Invalid or missing token"}, status=401)

        data = {
            "username": user.username,
            "email": user.email,
            "id": user.id,
            "exp": exp,
            "groups": groups,
            # "permissions": permissions
        }

        return Response(data)
