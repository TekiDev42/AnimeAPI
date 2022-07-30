from rest_framework import serializers

from api.models import Anime


class AnimeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Anime
        fields = [
            'id', 'nom', 'nom_original',
            'nombres_saisons', 'status',
            'status_anime', 'url', 'plateforme',
        ]
