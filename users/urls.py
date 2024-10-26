from django.urls import path, include
from users.views import (
    registration, api_reg, home_view, api_auth, authorization, deauth, get_position
)

urlpatterns = [
    path('', registration, name='reg'),
    path('home', home_view, name='home'),
    path('auth', authorization, name='auth'),
    path('deauth', deauth, name='deauth')
    
]

api = [
    path('api/v1/registration', api_reg, name='api_reg'),
    path('api/v1/authorization', api_auth, name='api_auth'),
    path('users/api/v1/getPosition', get_position, name='get_position'),
]
