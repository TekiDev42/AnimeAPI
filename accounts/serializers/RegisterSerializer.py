"""
API REST USER
"""
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from rest_framework import serializers

from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    useremail = serializers.EmailField(write_only=True, required=True, validators=[validate_email])

    class Meta:
        model = User
        fields = ('username', 'password', 'useremail')

        @staticmethod
        def validate(self, attr):
            if attr['password'] != attr['password2']:
                raise serializers.ValidationError({
                    "password": _("Password fields didn't match")
                })
            return attr

        @staticmethod
        def create(validated):
            user = User.objects.create(
                username=validated['username'],
                useremail=validated['email']
            )
            user.set_password(validated['password'])
            user.save()

            return user