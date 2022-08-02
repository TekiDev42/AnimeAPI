from pprint import pprint

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import IntegrityError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from accounts.serializers.RegisterSerializer import UserSerializer
from api.models import Anime, Plateforme
from api.serializers.PlateformeSerializer import PlateformeSerializer


class AnimesSerializer(serializers.ModelSerializer):
    plateforme = PlateformeSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Anime
        fields = [
            'id', 'nom', 'nom_original', 'description',
            'nombres_saisons', 'status',
            'status_anime', 'url', 'plateforme', 'user'
        ]


class AddAnimeSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(write_only=True, required=True, validators=[UnicodeUsernameValidator])
    nom_original = serializers.CharField(write_only=True, validators=[UnicodeUsernameValidator])
    description = serializers.CharField(write_only=True, validators=[UnicodeUsernameValidator])
    nombres_saisons = serializers.IntegerField(write_only=True)
    status = serializers.BooleanField(write_only=True)
    status_anime = serializers.BooleanField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    plateforme_name = serializers.CharField(write_only=True)

    class Meta:
        model = Anime
        fields = (
            'nom', 'nom_original', 'description',
            'nombres_saisons', 'status', 'status_anime',
            'user_id', 'plateforme_name'
        )

    def validate(self, attr) -> list:
        plateforme = Plateforme.objects.all()
        plateforme = plateforme.get(plateforme_name=attr['plateforme_name'])

        if not plateforme:
            raise serializers.ValidationError(
                {"plateforme": "This platform does not exist."})

        attr['plateforme_name'] = plateforme.id

        return attr

    def create(self, validated) -> Response:
        anime = self.Meta.model.objects.create(
            nom=validated['nom'],
            nom_original=validated['nom_original'],
            description=validated['description'],
            nombres_saisons=validated['nombres_saisons'],
            status=validated['status'],
            status_anime=validated['status_anime'],
            user_id=validated['user_id'],
            plateforme_id=validated['plateforme_name'],
        )

        anime.save()
        return Response(data=anime, status=status.HTTP_201_CREATED, content_type="application/json")