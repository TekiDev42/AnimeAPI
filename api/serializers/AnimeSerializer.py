from pprint import pprint

from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.response import Response

from accounts.models import User
from api.models import Anime, Plateforme
from api.serializers.PlateformeSerializer import PlateformeSerializer


class AnimeSerializer(serializers.ModelSerializer):
    plateforme = PlateformeSerializer(read_only=True)

    class Meta:
        model = Anime
        fields = [
            'id', 'nom', 'nom_original', 'description',
            'nombres_saisons', 'status',
            'status_anime', 'url', 'plateforme'
        ]


class AnimeCurrentUserDefault(CurrentUserDefault):
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class AddAnimeSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(write_only=True, required=True, validators=[UnicodeUsernameValidator])
    nom_original = serializers.CharField(write_only=True, validators=[UnicodeUsernameValidator])
    description = serializers.CharField(write_only=True, validators=[UnicodeUsernameValidator])
    nombres_saisons = serializers.IntegerField(write_only=True)
    status = serializers.BooleanField(write_only=True)
    status_anime = serializers.BooleanField(write_only=True)
    user = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=serializers.CurrentUserDefault())
    plateforme = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Anime
        depth = 1
        fields = (
            'nom', 'nom_original', 'description',
            'nombres_saisons', 'status', 'status_anime',
            'user', 'plateforme',
        )

    """def validate(self, attr):

        attr['plateforme'] = Plateforme.objects.get(id=attr['plateforme'])
        attr['user'] = User.objects.get(id=attr['user']).id

        return attr"""

    def create(self, validated):
        anime = Anime.objects.create(
            nom=validated['nom'],
            nom_original=validated['nom_original'],
            description=validated['description'],
            nombres_saisons=validated['nombres_saisons'],
            status=validated['status'],
            status_anime=validated['status_anime'],
            plateforme=validated['plateforme'],
            user=validated['user']
        )
        anime.save()
        return anime
