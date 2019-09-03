from rest_framework import mixins, viewsets

from .models import Listing, Starship
from .serializers import ListingSerializer, StarshipSerializer


class ListingViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()
