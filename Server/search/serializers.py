from rest_framework import serializers
from menus.models import Food
from image_adapter import ImageIncoder
class FoodSerializer(serializers.ModelSerializer):
    # image = serializers.CharField(read_only=True)
    imageIncoder = ImageIncoder()
    image = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = '__all__'
    
    def get_image(self, obj):
        return self.imageIncoder.getBase64String(obj.foodName)
