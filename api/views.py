from django.shortcuts import render
from rest_framework import viewsets, permissions

from accounts.models import User
from api.models import Anime
from api.serializers.serializers import UserSerializer, AnimeSerializer


def index(request):
    return render(request, 'api/index.html', context={})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [permissions.IsAuthenticated]

