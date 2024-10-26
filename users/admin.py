from django.contrib import admin
from users.models import Taxist, Courier, Client

class TaxistAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'name', 'password', 'rating', 'bank', 'is_free')
    list_display_links = ('id', 'name', 'number')
    search_fields = ('name', 'number')

admin.site.register(Taxist, TaxistAdmin)

class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'name', 'password', 'rating', 'bank')
    list_display_links = ('id', 'name', 'number')
    search_fields = ('name', 'number')

admin.site.register(Courier, CourierAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'name', 'password', 'rating', 'bank')
    list_display_links = ('id', 'name', 'number')
    search_fields = ('name', 'number')

admin.site.register(Client, ClientAdmin)