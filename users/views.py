from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile

def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'users/profile.html', {'profile': profile})
