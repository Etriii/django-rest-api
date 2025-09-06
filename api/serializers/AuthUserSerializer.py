from rest_framework import serializers

class AuthUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    id = serializers.IntegerField()
    exp = serializers.IntegerField()
    groups = serializers.ListField(child=serializers.CharField())
