from rest_framework import serializers

from api.models import Plateforme


class PlateformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plateforme
        fields = [
            'id', 'plateforme', 'plateforme_url'
        ]
