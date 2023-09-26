from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    sku=models.CharField(max_length=25, unique=True)
    current_stock=models.PositiveIntegerField(default=0)
    low_stock_number=models.PositiveIntegerField(default=10)
