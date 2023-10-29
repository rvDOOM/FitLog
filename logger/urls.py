from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "logger"

urlpatterns = [
    path("session/", views.create_session, name="session"),
]
