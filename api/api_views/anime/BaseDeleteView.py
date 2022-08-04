from pprint import pprint

from django.http import Http404

from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response

from api.api_views.anime.base_class import BaseAnimeView
from api.models import Anime


class AnimeDeleteView(BaseAnimeView, RetrieveUpdateDestroyAPIView):
    def delete_(self, instance: Anime):
        delete = self.perform_destroy(instance)
        if not delete:
            return Response(status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk=None) -> Anime | Http404:
        try:
            return Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            raise Http404

    def perform_destroy(self, instance: Anime):
        delete = instance.delete()
        return delete

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(kwargs['pk'])

        if instance:
            self.delete_(instance)

        return Response(status=status.HTTP_404_NOT_FOUND)
