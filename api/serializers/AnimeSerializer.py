from pprint import pprint

from rest_framework import serializers

from accounts.serializers.RegisterSerializer import UserSerializer
from api.models import Anime
from api.serializers.PlateformeSerializer import PlateformeSerializer


class AnimesSerializer(serializers.ModelSerializer):

    plateforme = PlateformeSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    queryset = Anime.objects.all()

    class Meta:
        model = Anime
        fields = [
            'id', 'nom', 'nom_original', 'description',
            'nombres_saisons', 'status',
            'status_anime', 'url', 'plateforme', 'user'
        ]