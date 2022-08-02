from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from api.api_views.anime.base_class import BaseAnimeView
from api.serializers.AnimeCreateSerializer import AnimeCreateSerializer


class AnimeCreateView(BaseAnimeView, CreateAPIView):

    def create(self, request, *args, **kwargs) -> Response:
        serializer = AnimeCreateSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=False):
            return Response({"error": "Data is not valid"}, status=status.HTTP_400_BAD_REQUEST)

        if not self.perform_create(serializer):
            return Response({'error': 'The query failed'}, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_success_headers(self, data) -> dict:
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def perform_create(self, serializer: AnimeCreateSerializer) -> bool:
        try:
            serializer.save()
        except IntegrityError as error:
            return False
        return True
