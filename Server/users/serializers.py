from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username','password', 'name', 'birthDate', 'height', 'weight', 'activity', 'gender', 'preference', 'kcal',)

class UserProfileSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('password','height', 'weight', 'activity')