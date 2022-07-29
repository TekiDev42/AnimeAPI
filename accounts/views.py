from django.contrib.auth import logout, login

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _

from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator

from accounts.models import User
from accounts.utils import fields_is_not_empty, fields_validator


def create_user(request):
    if request.method == 'POST':

        username = escape(request.POST.get('username'))
        user_email = escape(request.POST.get('useremail'))
        password = escape(request.POST.get('password'))

        """
            List of tuples with values + validation functions
            (Value + Validator function)
        """
        fields = [
            (username, UnicodeUsernameValidator),
            (password, validate_password),
            (user_email, validate_email),
        ]

        fields_status = fields_is_not_empty([fields[0][0], fields[1][0], fields[2][0]])

        if not fields_status:
            return HttpResponse(_("Required fields are not valid"), status=400)

        has_error, message = fields_validator(fields)

        if not has_error:
            return HttpResponse(_(message), status=409)

        new_user, created = User.objects.get_or_create(username=username, password=password, email=user_email)

        if created:
            login(request, new_user)
            return HttpResponse(_('Account has been created'), status=200)

        if new_user and not created:
            return HttpResponse(_('This user is already used.'), status=400)

    return HttpResponse(_('An error has occurred, please try again'), status=409)


def logout_user(request):
    logout(request)
    return redirect('home')
