from django.urls import path

from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('transactions/add/', TransactionAdd.as_view(), name='transactions-add'),
    path('transactions/history/', TransactionHistory.as_view(), name='transactions-history'),
    path('transactions/<int:pk>/', TransactionEdit.as_view(), name='transactions-edit'),
    path('category/add/', CategoryAdd.as_view(), name='category-add'),
    path('category/<int:pk>/', Category.as_view(), name='category'),
    path('report/generate/', ReportGenerate.as_view(), name='report-generate'),
    path('report/export/', ReportExport.as_view(), name='report-export'),
]