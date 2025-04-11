from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.restaurant_name}"