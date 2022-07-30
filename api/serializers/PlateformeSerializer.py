from rest_framework import serializers

from api.models import Plateforme


class PlateformeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Plateforme
        fields = [
            'id', 'plateforme', 'plateforme_url'
        ]
