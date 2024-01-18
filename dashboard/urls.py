from django.urls import path, include

from .views import *


urlpatterns = [
    path('transactions/add/', TransactionAdd.as_view(), name='transactions-add'),
]