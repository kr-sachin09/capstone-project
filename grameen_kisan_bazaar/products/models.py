from django.db import models
from core.models import CustomUser # CustomUser मॉडल को आयात करें

class Product(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'farmer'})
    name = models.CharField(max_length=200)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, default='kg') # जैसे kg, quintal
    description = models.TextField()
    crop_type = models.CharField(max_length=100, blank=True, null=True) # जैसे Long Grain
    usage = models.CharField(max_length=200, blank=True, null=True) # जैसे Pilafs, Biryanis
    storage_info = models.CharField(max_length=200, blank=True, null=True) # जैसे Store in a cool, dry place
    location = models.CharField(max_length=200) # किसान का स्थान
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    harvest_date = models.DateField(blank=True, null=True)
    estimated_delivery = models.CharField(max_length=100, blank=True, null=True) # जैसे July 20-22

    def __str__(self):
        return self.name