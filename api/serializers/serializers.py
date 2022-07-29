from rest_framework import serializers

from accounts.models import User
from api.models import Anime


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = [
            'nom', 'nom_original',
            'nombres_saisons', 'plateforme',
            'plateforme_url', 'status',
            'status_anime', 'url'
        ]
