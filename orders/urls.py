from django.urls import path, include
from orders.views import (
    api_call_taxi, api_start_order, api_end_order, api_make_order
)

urlpatterns = [
    
]

api = [
    path('api/v1/call_taxi/<str:taxistId>/', api_call_taxi, name='api_call_taxi'),
    path('api/v1/make_order/<str:taxistId>/', api_make_order, name='api_make_order'),
    path('api/v1/start_order/<str:orderId>/', api_start_order, name='api_start_order'),
    path('api/v1/end_order/<str:orderId>/', api_end_order, name='api_end_order'),
]