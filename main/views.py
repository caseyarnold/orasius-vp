from django.shortcuts import render, get_object_or_404
from auths.models import Profile

def home(req):
    return render(req, "main/home.html")
home.login_required = False

def profile(req, username):
    try:
        profile = Profile.objects.get(user__username=username, user__is_active=True)
    except Profile.DoesNotExist:
        return render(req, "main/profile_not_found.html")

    return render(req, "main/profile.html", {'profile': profile})

profile.login_required = False
