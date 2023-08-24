from rest_framework import serializers
from ..models import User, Menu

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class MenuSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"