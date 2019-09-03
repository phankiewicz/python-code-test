from rest_framework.serializers import ModelSerializer

from .models import Starship


class StarshipSerializer(ModelSerializer):
    class Meta:
        model = Starship
        fields = (
            'starship_class',
            'manufacturer',
            'length',
            'hyperdrive_rating',
            'cargo_capacity',
            'crew',
            'passengers',
        )
