from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import *


class TransactionAdd(CreateView):
    form_class = TransactionForm
    template_name = 'add_transaction.html'
    success_url = reverse_lazy('index')


class TransactionHistory(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_history.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(author=user)
        return queryset


class TransactionEdit(UpdateView):
    model = Transaction
    template_name = 'edit_transaction.html'
    fields = '__all__'
