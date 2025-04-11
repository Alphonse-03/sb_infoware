from django.db import models
from restaurant.models import Restaurant

# Create your models here.
class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=100)
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Dish name {self.dish_name} by {self.restaurant_name.restaurant_name}"