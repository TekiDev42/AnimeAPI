"""
API REST USER
"""
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from rest_framework import serializers

from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    email = serializers.EmailField(write_only=True, required=True, validators=[validate_email])

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

        """@staticmethod
        def validate(self, attr):
            if attr['password'] != attr['password2']:
                raise serializers.ValidationError({
                    "password": _("Password fields didn't match")
                })
            return attr"""

    def create(self, validated):
        user = User.objects.create(
            username=validated['username'],
            email=validated['email']
        )
        user.set_password(validated['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
