from rest_framework.serializers import ModelSerializer

from .models import Listing, Starship


class ListingSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = ('name', 'ship_type', 'price', 'active', 'created')


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
