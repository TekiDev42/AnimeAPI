from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models import Plateforme
from api.serializers import PlateformeSerializer


class PlateformeViewSet(ModelViewSet):
    serializer_class = PlateformeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Plateforme.objects.all().order_by('plateforme_name')

    def get_queryset(self):
        return Plateforme.objects.all().order_by('plateforme_name')
