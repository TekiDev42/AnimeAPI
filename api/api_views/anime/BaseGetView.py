from pprint import pprint

from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.api_views.anime.base_class import BaseAnimeView
from api.models import Anime


class AnimeGetView(BaseAnimeView, ListAPIView):

    def get_object(self, pk=None):
        pprint(pk)
        try:
            return Anime.objects.get(pk=pk)
        except Anime.DoesNotExist:
            raise Http404

    def list(self, request, *args, **kwargs):
        anime = self.get_object(kwargs['pk'])
        serializer = self.serializer_class(anime)
        return Response(serializer.data, status=status.HTTP_200_OK)
