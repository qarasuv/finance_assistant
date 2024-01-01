from django.urls import path, include
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('registration/', Register.as_view(), name='registration')
]