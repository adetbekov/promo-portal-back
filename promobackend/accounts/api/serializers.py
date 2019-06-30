from rest_framework import serializers

from django.contrib.auth.models import User
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ["city_name"]
        
    def get_city_name(self, obj):
        return obj.city.name


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)
    phone = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ["id", "phone", "first_name", "last_name", "email", "profile"]
