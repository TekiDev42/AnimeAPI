from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.utils.html import escape


def login_user(request):
    if request.method == "POST":
        username = escape(request.POST.get('username'))
        password = escape(request.POST.get('password'))
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

    return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')

