from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import *


class TransactionAdd(CreateView):
    form_class = TransactionForm
    template_name = 'add_transaction.html'
    success_url = reverse_lazy('index')
