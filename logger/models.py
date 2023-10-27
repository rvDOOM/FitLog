from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Session(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(required=False)


class Workout(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)


class Sets(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    reps_completed = models.IntegerField(max_length=3)
