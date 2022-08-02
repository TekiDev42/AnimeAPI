from pprint import pprint

from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Anime
from api.serializers.AnimeSerializer import AnimesSerializer


class AnimeGetView(ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimesSerializer
    permission_classes = [IsAuthenticated]

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
