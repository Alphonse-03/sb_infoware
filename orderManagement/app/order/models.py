from django.db import models
from restaurant.models import Restaurant
from dish.models import Dish    
# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish_name = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer_name}"