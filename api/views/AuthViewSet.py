from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..utils.token_extractor import get_user_from_token

class AuthViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        user, exp, groups = get_user_from_token(request) #, groups, permissions
        
        if not user:
            return Response({"error": "Invalid or missing token"}, status=401)

        return Response({
            "username": user.username,
            "email": user.email,
            "id": user.id,
            "exp": exp,
            "groups": groups
            # "permissions": permissions
        })

    