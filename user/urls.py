from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
]
