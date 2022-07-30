from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.models import Anime, Plateforme
from api.serializers import PlateformeSerializer
from api.serializers.AnimeSerializer import AnimeSerializer


def index(request):
    return render(request, 'api/index.html', context={})


class PlateformeViewSet(ModelViewSet):
    serializer_class = PlateformeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Plateforme.objects.all().order_by('plateforme')

    def get_queryset(self):
        return Plateforme.objects.all().order_by('plateforme')


class AnimeViewSet(ModelViewSet):
    serializer_class = AnimeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Anime.objects.all().order_by('nom')

    def get_queryset(self):
        user_id: int = self.request.user.id
        return Anime.objects.filter(user__anime=user_id)

