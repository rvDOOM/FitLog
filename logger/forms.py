from unittest import SkipTest
from django.db.models.fields import forms
from .models import Session, Workout, Sets


class CreateSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ["description"]


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["exercise_name"]


class CreateSetForm(forms.ModelForm):
    class Meta:
        model = Sets
        fields = ["weight", "reps_completed"]
