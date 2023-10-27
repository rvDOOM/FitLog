from django.contrib.auth import login
from django.shortcuts import render
from .models import Session, Workout, Sets
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from .forms import CreateSessionForm, CreateWorkoutForm, CreateSetForm

# Create your views here.


@login_required
def create_session(request):
    if request.method == "POST":
        form = CreateSessionForm(request.POST)
        if form.is_valid():
            new_session = Session(
                user=request.user,
                date=timezone.now().date(),
                description=form.cleaned_data["description"],
            )
            new_session.save()
            ## TODO: ADD A REDIRECTION
    else:
        form = CreateSessionForm()

    return None


@login_required
def create_workout(request, curr_session):
    if request.method == "POST":
        form = CreateWorkoutForm(request.POST)
        if form.is_valid():
            new_workout = Workout(
                session=curr_session, exercise_name=form.cleaned_data["exercise_name"]
            )
            new_workout.save()
            ## TODO: ADD A REDIRECTION
    else:
        form = CreateWorkoutForm()

    return None


@login_required
def create_set(request, curr_workout):
    if request.method == "POST":
        form = CreateSetForm(request.POST)
        if form.is_valid():
            new_set = Sets(
                workout=curr_workout,
                weight=form.cleaned_data["weight"],
                reps_completed=form.cleaned_data["reps_completed"],
            )
            new_set.save()
    else:
        form = CreateSetForm()

    return None
