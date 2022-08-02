from rest_framework import serializers
from api.models import Anime


class AnimeCreateSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(required=True, max_length=128)
    nom_original = serializers.CharField(required=False, max_length=128, default="")
    description = serializers.CharField(required=False, max_length=128, default="")
    nombres_saisons = serializers.IntegerField(required=True)
    status = serializers.BooleanField(required=True)
    status_anime = serializers.BooleanField(required=True)
    url = serializers.URLField(required=False, default="")
    plateforme_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)

    queryset = Anime.objects.all()

    class Meta:
        model = Anime
        fields = [
            'nom', 'nom_original', 'description',
            'nombres_saisons', 'status',
            'status_anime', 'url', 'plateforme_id', 'user_id'
        ]
