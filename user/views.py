from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("profile:create"))  # Redirect to the homepage
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect(
                "profile:view", user_profile_id=user.id
            )  # Redirect to the homepage
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})
