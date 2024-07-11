from django.contrib import admin

from .models import Bicycle, PriceType, RentedBicycle


class PriceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', )
    empty_value_display = '-пусто-'


class BicycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'rental_cost',
                    'status',)
    empty_value_display = '-пусто-'


class RentedBicycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'bicycle', 'rented_at',
                    'status', 'returned_at', )
    empty_value_display = '-пусто-'


admin.site.register(PriceType, PriceTypeAdmin)
admin.site.register(Bicycle, BicycleAdmin)
admin.site.register(RentedBicycle, RentedBicycleAdmin)
