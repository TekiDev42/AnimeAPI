from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from api.api_views.anime.base_class import BaseAnimeView
from api.models import Anime
from api.serializers.AnimeSerializer import AnimesSerializer


class AnimeRetrieveView(BaseAnimeView, RetrieveAPIView):

    def get_object(self):
        return Anime.objects.all()

    def retrieve(self, request, *args, **kwargs):
        animes = self.get_object()
        serialized = AnimesSerializer(animes, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
