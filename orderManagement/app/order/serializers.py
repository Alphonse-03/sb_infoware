from rest_framework import serializers
from .models import Orders
from restaurant.models import Restaurant
from dish.models import Dish

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class CreateOrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(max_length=100,min_length=3)
    restaurant_name = serializers.IntegerField()
    dish_name = serializers.IntegerField()
    def validate(self, data):
        if not Restaurant.objects.filter(restaurant_id=data['restaurant_name']).exists():
            raise serializers.ValidationError("Restaurant does not exist")
        if not Dish.objects.filter(dish_id=data['dish_name'],restaurant_name__restaurant_id=data['restaurant_name']).exists():  
            raise serializers.ValidationError("Dish does not exist in given restaurant.")
        

        return data
    class Meta:
        model = Orders
        fields = '__all__'

class OrdersIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
    def validate(self, data):   
        # Custom validation logic (if any)
        return data
