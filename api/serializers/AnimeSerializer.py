from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

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
    user_id = serializers.IntegerField(write_only=True, default=AnimeCurrentUserDefault())
    plateforme_id = serializers.CharField(write_only=True)

    class Meta:
        model = Anime
        depth = 1
        fields = (
            'nom', 'nom_original', 'description',
            'nombres_saisons', 'status', 'status_anime',
            'plateforme_id', 'user_id'
        )

    def validate(self, attr):
        try:
            plateforme = Plateforme.objects.get(plateforme__exact=attr['plateforme_id'])
        except Plateforme.DoesNotExist:
            raise serializers.ValidationError(
                {"plateforme": "This platform does not exist."})

        if self.context['request'].user.id != attr['user_id']:
            raise serializers.ValidationError(
                {"user": "Who are you?!??"})

        attr['plateforme_id'] = plateforme.id
        return attr

    def create(self, validated):
        anime = Anime.objects.create(
            nom=validated['nom'],
            nom_original=validated['nom_original'],
            description=validated['description'],
            nombres_saisons=validated['nombres_saisons'],
            status=validated['status'],
            status_anime=validated['status_anime'],
            user_id=validated['user_id'],
            plateforme_id=validated['plateforme_id'],
        )
        anime.save()
        return anime
