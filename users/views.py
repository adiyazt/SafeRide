from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest,HttpResponseForbidden, HttpResponseNotAllowed
from users.models import Client, Taxist, Courier
from orders.models import TaxiOrder, DeliveryOrder
import json

def authorization(request):
    template = 'auth.html'
    if request.session.get('is_authorized'):
        return HttpResponseRedirect(redirect_to='/users/home')
    return render(request, template)


def registration(request):
    template = 'reg.html'
    if request.session.get('is_authorized'):
        return HttpResponseRedirect(redirect_to='/users/home')
    return render(request, template)


def deauth(request):
    if request.session.get('is_authorized'):
        request.session.clear()
    return HttpResponseRedirect(redirect_to='/users/')


def api_auth(request):
    number  : str = request.POST.get('number')
    password: str = request.POST.get('password')

    if number and password:
        if Client.objects.filter(number=number, password=password).exists():
            user = Client.objects.get(number=number, password=password)
            kind = 'client'
        elif Taxist.objects.filter(number=number, password=password).exists():
            user = Taxist.objects.get(number=number, password=password)
            kind = 'taxist'
        elif Courier.objects.filter(number=number, password=password).exists():
            user = Courier.objects.get(number=number, password=password)
            kind = 'courier'
        else:
            return HttpResponseNotAllowed('User is not exists')
        
        request.session['is_authorized'] = True
        request.session['number'] = user.number
        request.session['user_id'] = str(user.pk)
        request.session['kind'] = kind

        return HttpResponseRedirect('/users/home')
        
    return HttpResponseBadRequest('Invalid data',)


def api_reg(request):
    name      : str = request.POST.get('name')
    number    : str = request.POST.get('number')
    password1 : str = request.POST.get('password1')
    password2 : str = request.POST.get('password2')
    kind      : str = request.POST.get('kind')

    if name and number and password1 and password2 and kind:
        if Client.objects.filter(number=number).exists() or Taxist.objects.filter(number=number).exists() or Courier.objects.filter(number=number).exists():
            return HttpResponse('User exists', status=403)

    if not password1 == password2:
        return HttpResponse('Passwords do not match', status=403)
    
    if kind=='client':
        user: Client = Client()
    elif kind=='taxist':
        user: Taxist = Taxist()
    elif kind=='courier':
        user: Courier = Courier()
    else:
        return HttpResponse('Something went wrong', status=403)
    
    user.number = number
    user.name = name
    user.password = password1
    if user.is_valid():
        user.save()

        request.session['is_authorized'] = True
        request.session['number'] = user.number
        request.session['user_id'] = str(user.pk)
        request.session['kind'] = kind
        return HttpResponseRedirect(redirect_to='/users/home/')
    else:
        return HttpResponse('Invalid data', status=403)



def home_view(request):
    if request.session.get('is_authorized'):
        context = {
            'number' : 1,
            'csrf_token' : '7893yre788u2dgh178b87'
        }
        kind = request.session.get('kind')
        if kind == 'client':
            template = 'client.html'
            context = {
                'taxists' : Taxist.objects.filter(is_free=True)
            }
        elif kind == 'taxist' or "courier":
            template = 'taxcour.html'
            context = {
                'orders' : TaxiOrder.objects.filter(taxist=request.session.get('user_id'))
            }
        return render(request, template_name=template, context=context)
    
    return HttpResponseRedirect(redirect_to='auth')


def get_position(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        position = data.get('position')
        if request.session.get('kind') == 'taxist':
            taxist = Taxist.objects.get(pk=request.session.get('user_id'))
            taxist.position = position
        if request.session.get('kind') == 'client':
            client = Client.objects.get(pk=request.session.get('user_id'))
            client.position = position
        print(position)

        return HttpResponse('Well')
    except Exception as e:
        return HttpResponse('Error', status=500)