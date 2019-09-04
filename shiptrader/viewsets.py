from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from .filters import ListingFilter
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
    filterset_class = ListingFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('price', 'created')


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()
