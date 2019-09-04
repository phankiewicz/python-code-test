from django_filters import rest_framework as filters

from .models import Starship


class ListingFilter(filters.FilterSet):
    price = filters.RangeFilter()
    created = filters.DateTimeFromToRangeFilter()
    ship_type__starship_class = filters.ChoiceFilter(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['ship_type__starship_class'].extra['choices'] = [
            (starship_class, starship_class)
            for starship_class in Starship.objects.values_list(
                'starship_class', flat=True
            ).distinct()
        ]
