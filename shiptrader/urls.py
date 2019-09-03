from rest_framework import routers

from django.conf.urls import include, url

from .viewsets import ListingViewSet, StarshipViewSet

router_v1 = routers.DefaultRouter()

router_v1.register(r'listings', ListingViewSet, base_name='listing')
router_v1.register(r'starships', StarshipViewSet, base_name='starship')


urlpatterns = (url(r'^v1/', include(router_v1.urls, namespace='v1_shiptrader')),)
