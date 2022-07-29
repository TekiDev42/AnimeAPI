from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from accounts.utils import validation_fields


def create_user(request):
    if request.method == 'POST':

        username = escape(request.POST.get('username'))
        user_email = escape(request.POST.get('useremail'))
        password = escape(request.POST.get('password'))

        fields_is_valid = validation_fields([username, user_email, password])

        if not fields_is_valid:
            return HttpResponse(_("Required fields are not valid"), status=400)

        new_user = User.objects.create_user(username=username, password=password, email=user_email)

        if new_user:
            login(request, new_user)
            return HttpResponse(_('Account has been created'), status=200)

    return HttpResponse(_('An error has occurred, please try again'), status=409)


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
