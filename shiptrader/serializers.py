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

    def to_internal_value(self, data):
        for field, value in data.items():
            if str(value).lower() == 'unknown':
                data[field] = None
            try:
                input_without_commas = int(str(value).replace(',', ''))
                data[field] = input_without_commas
            except ValueError:
                pass
        return super().to_internal_value(data)
