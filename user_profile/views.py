from urllib.request import HTTPError
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import UserProfileForm
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def create_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            user_profile_id = profile.id
            return redirect("profile:view", user_profile_id=user_profile_id)
    else:
        # Check to see if user has already created a profile
        # if profile exists route to view profile
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            return redirect("profile:view", user_profile_id=user_profile.id)
        except UserProfile.DoesNotExist:
            form = UserProfileForm()

    return render(request, "user_profile/create_profile.html", {"form": form})


@login_required
def view_profile(request, user_profile_id):
    user_profile = get_object_or_404(UserProfile, id=user_profile_id)

    if user_profile.user == request.user:
        return render(
            request, "user_profile/view_profile.html", {"user_profile": user_profile}
        )
    else:
        return HttpResponse("Access Denied.")


@login_required
def edit_profile(request):
    return HttpResponse("Edit Profile Page")
