from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.urls import reverse


class UserProfileTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@email.com", password="testpassword1"
        )

        self.profile = UserProfile.objects.create(
            user=self.user, weight=70.0, height=170.0, age=25
        )

    def test_create_profile_view(self):
        self.client.login(email="test@email.com", password="testpassword1")

        response = self.client.post(
            reverse("profile:create"),
            {"weight": 75.0, "height": 175.0, "age": 30},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())

    def test_view_profile_view(self):
        self.client.login(email="test@email.com", password="testpassword1")

        response = self.client.get(reverse("profile:view", args=[self.user.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_profile/view_profile.html")

    def test_edit_profile_view(self):
        self.client.login(email="test@email.com", password="testpassword1")

        response = self.client.get(reverse("profile:edit"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_profile/edit_profile.html")
