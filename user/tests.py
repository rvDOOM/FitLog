from django.db import IntegrityError
from django.test import TestCase
from .models import CustomUser
from django.contrib.auth import get_user_model

# Create your tests here.


class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="example@test.com", password="Thisisjustatest1"
        )

    def test_create_user(self):
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_empty_email(self):
        with self.assertRaises(IntegrityError):
            self.user = CustomUser.objects.create_user(email="")

    def test_dupe(self):
        with self.assertRaises(ValueError):
            self.user = CustomUser.objects.create_user(
                email="example@test.com", password="Thisshouldnotwork"
            )
