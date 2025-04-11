from rest_framework import serializers
from .models import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['dish_id', 'dish_name', 'restaurant_name', 'price']   

class DishOrderSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Custom validation logic (if any)
        return data
    class Meta:
        model = Dish
        fields = '__all__'