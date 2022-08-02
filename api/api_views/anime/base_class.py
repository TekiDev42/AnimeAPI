from rest_framework.permissions import IsAuthenticated

from api.models import Anime
from api.serializers.AnimeSerializer import AnimesSerializer


class BaseAnimeView:
    queryset = Anime.objects.all()
    serializer_class = AnimesSerializer
    permission_classes = [IsAuthenticated]
