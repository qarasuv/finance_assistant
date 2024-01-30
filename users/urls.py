from django.urls import path, include

from .views import *


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', Register.as_view(), name='registration')
]