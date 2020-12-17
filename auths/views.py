from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_user(req):
    # the user wants the form
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(req, user)
                messages.success(req, "Logged in successfully!")

                url = req.GET.get('next')

                if url is not None: return redirect(url)

                return redirect("/")
            else:
                messages.error(req, "You have been suspended!")
                return redirect(login_user)
        else:
            messages.error(req, "Hmmmm...are you sure you typed everything in correctly?")
            return redirect(login_user)


    return render(req, "auths/login.html")

login_user.login_required = False

def logout_user(req):
    messages.info(req, "You have been logged out. Come again soon, %s!" % req.user.username)
    logout(req)
    return redirect("/")