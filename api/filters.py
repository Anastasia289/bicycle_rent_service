# from django_filters import (BooleanFilter, CharFilter, FilterSet,
#                             ModelMultipleChoiceFilter)

# from bicycles.models import Bicycle, RentedBicycle


# class BicyclesFilter(FilterSet):
#     """Фильтр для велосипедов."""

#     is_rented = BooleanFilter(method='get_is_favorited')

#     class Meta:
#         model = Bicycle
#         fields = ('name', 'description', 'rental_cost',
#                   'status', 'is_rented')

#     def get_is_rented(self, queryset, name, value):
#         return queryset.filter(rentedbicycle__bicycle=self.request.user)
