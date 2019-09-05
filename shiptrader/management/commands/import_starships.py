import requests

from django.conf import settings
from django.core.management.base import BaseCommand

from shiptrader.serializers import StarshipSerializer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = settings.STARSHIPS_API_URL

        while url is not None:
            response = requests.get(url)

            results = response.json()['results']
            url = response.json()['next']

            for result in results:
                serializer = StarshipSerializer(data=result)
                serializer.is_valid(raise_exception=True)
                serializer.save()
