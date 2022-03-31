from rest_framework import serializers
from .models import WeekMenu

class WeekMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeekMenu
        fields = '__all__'
        read_only_field = '__all__'