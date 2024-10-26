from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest,HttpResponseForbidden, HttpResponseNotAllowed
from users.models import Client, Taxist, Courier
from orders.models import TaxiOrder, DeliveryOrder
from .functions import get_distance
from datetime import datetime

def api_call_taxi(request, taxistId = None):
    if taxistId:
        if request.session.get('is_authorized'):
            context = {
                'taxistId' : taxistId
            }
            return render(request, template_name='make_order.html', context=context)
        return HttpResponseRedirect('/users/')
    return HttpResponse('No taxist')


def api_make_order(request, taxistId = None):
    number = request.session.get('number')
    next_pos = request.GET.get('next_pos')
    geoposition = str(request.GET.get('geoposition'))

    geoposition = geoposition.split(' ')
    next_pos = next_pos.split(' ')
    lat1 = float(geoposition[0])
    lat2 = float(next_pos[0])
    lon1 = float(geoposition[1])
    lon2 = float(next_pos[1])

    distance = round(get_distance(lat1, lat2, lon1, lon2), 1)
    price = round(distance * 500, 3)

    taxi_order: TaxiOrder = TaxiOrder()
    taxi_order.number = number
    taxi_order.client = Client.objects.get(pk=request.session.get('user_id'))
    taxi_order.distance = distance
    taxi_order.price = price
    taxi_order.taxist = taxistId
    taxi_order.is_active = True
    
    taxist = Taxist.objects.get(pk=taxistId)
    taxist.is_free = False
    

    taxi_order.save()

    context = {
        'distance' : distance,
        'price' : price,
        'taxist' : taxist.name,
        'order' : taxi_order,
        'is_taxist' : False
    }

    return render(request, context=context, template_name='order.html')
    


def api_start_order(request, orderId = None):
    order = TaxiOrder.objects.get(pk=orderId)
    context = {
        'distance' : order.distance,
        'price' : order.price,
        'taxist' : Taxist.objects.get(pk=request.session.get('user_id')).name,
        'order' : order,
        'is_taxist' : True
    }
    return render(request, context=context, template_name='order.html')


def api_end_order(request, orderId=None):
    print(0000000000000000000000000000000000000000000000000000000)
    order = TaxiOrder.objects.get(pk=orderId)
    taxist = Taxist.objects.get(pk=order.taxist)
    client = Client.objects.get(name=order.client)
    
    taxist.is_free = True
    taxist.bank = taxist.bank + order.price
    taxist.save()
    
    order.is_active = False
    order.end = datetime.now()
    order.save()
    
    client.bank = client.bank - order.price
    client.save()
    
    return HttpResponseRedirect(redirect_to='/users/home')