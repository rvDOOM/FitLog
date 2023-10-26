from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.PositiveIntegerField()
