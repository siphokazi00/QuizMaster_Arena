from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        UserProfile.objects.create(user=user, bio="Test Bio")

    def test_user_profile_creation(self):
        user_profile = UserProfile.objects.get(user__username="testuser")
        self.assertEqual(user_profile.bio, "Test Bio")
