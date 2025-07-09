from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('buyer', 'Buyer'),
        ('farmer', 'Farmer'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='buyer')
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    crops_grown = models.TextField(blank=True, null=True) # केवल किसानों के लिए
    bio = models.TextField(blank=True, null=True) # केवल किसानों के लिए

    def __str__(self):
        return self.username
