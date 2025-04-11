from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantAddSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Custom validation logic (if any)
        return data
    class Meta:
        model = Restaurant
        fields = '__all__'