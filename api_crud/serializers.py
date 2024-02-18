# serializers.py

from rest_framework import serializers
from .models import NetworkAdmin, Router

class NetworkAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkAdmin
        fields = '__all__'

class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = '__all__'
