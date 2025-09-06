from rest_framework import serializers
from api.models import System

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = "__all__"
        
        read_only_fields = ["id", "created_at", "updated_at", "updated_by"]
        
