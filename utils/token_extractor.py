from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model

User = get_user_model()

def get_user_from_token(request):
    """
    Extracts the user and expiration from the JWT token in the Authorization header.
    Returns User object and expiration if valid, else None.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None, None  # Return both user and expiration as None if not present

    try:
        token = auth_header.split()[1]
        validated_token = UntypedToken(token)  
        
        exp = validated_token.payload.get("exp")
        groups = validated_token.payload.get("groups")
        permissions = validated_token.payload.get("permissions")
        
        jwt_auth = JWTAuthentication()
        user, _ = jwt_auth.get_user(validated_token), validated_token
        
        return user, exp, groups, permissions
    except (IndexError, InvalidToken, TokenError):
        return None, None
