from django.urls import path

from .views import *


urlpatterns = [
    path('transactions/add/', TransactionAdd.as_view(), name='transactions-add'),
    path('transactions/history/', TransactionHistory.as_view(), name='transactions-history'),
    path('transactions/<int:pk>/', TransactionEdit.as_view(), name='transactions-edit'),
    path('report/generate/', ReportGenerate.as_view(), name='report-generate'),

]