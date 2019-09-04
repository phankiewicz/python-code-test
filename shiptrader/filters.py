from django_filters import rest_framework as filters


class ListingFilter(filters.FilterSet):
    price = filters.RangeFilter()
