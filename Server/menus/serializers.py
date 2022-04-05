from rest_framework import serializers
from .models import Food, Menu, MenuToFood
from image_adapter import ImageIncoder
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = '__all__'
        # read_only_field = ('userId',)

class MenuToFoodSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model = MenuToFood
        fields = '__all__'

class FoodRecommSerializer(serializers.ModelSerializer):
    # image = serializers.CharField(read_only=True)
    imageIncoder = ImageIncoder()
    image = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = '__all__'
    def get_image(self, obj):
        return self.imageIncoder.getBase64String(obj.foodName)