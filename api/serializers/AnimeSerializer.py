from rest_framework import serializers

from api.models import Anime
from api.serializers.PlateformeSerializer import PlateformeSerializer


class AnimeSerializer(serializers.ModelSerializer):
    plateforme = PlateformeSerializer(read_only=True)

    class Meta:
        model = Anime
        fields = [
            'id', 'nom', 'nom_original',
            'nombres_saisons', 'status',
            'status_anime', 'url', 'plateforme'
        ]
