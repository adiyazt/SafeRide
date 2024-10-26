from django.contrib import admin
from orders.models import TaxiOrder, DeliveryOrder

class TaxiOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'taxist', 'distance', 'rating', 'price', 'is_active')
    list_display_links = ('id', 'distance', 'price')
    search_fields = ('price', 'distance')

admin.site.register(TaxiOrder, TaxiOrderAdmin)

class DeliveryOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'recipient', 'courier', 'distance', 'rating', 'price')
    list_display_links = ('id', 'distance', 'price')
    search_fields = ('price', 'distance')

admin.site.register(DeliveryOrder, DeliveryOrderAdmin)