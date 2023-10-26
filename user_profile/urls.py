from django.contrib import admin
from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path("create/", views.create_profile, name="create"),
    path("view/<int:user_profile_id>", views.view_profile, name="view"),
    path("edit_profile/", views.edit_profile, name="edit"),
]
