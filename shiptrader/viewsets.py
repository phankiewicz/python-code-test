from rest_framework import viewsets

from .models import Starship
from .serializers import StarshipSerializer


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()
