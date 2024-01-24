from datetime import datetime

from django.shortcuts import render
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


class ReportGenerate(ListView):
    template_name = 'report.html'
    context_object_name = 'report_data'

    def post(self, request, *args, **kwargs):
        date_range = self.request.POST.get('date_range')
        report_data = self.get_queryset(date_range)
        return render(request, self.template_name, {'report_data': report_data, 'date_range': date_range})

    def get_queryset(self, date_range=None):
        if date_range:
            from_date, to_date = map(lambda x: datetime.strptime(x.strip(), '%m/%d/%Y'), date_range.split('-'))
            from_date_str = from_date.strftime('%Y-%m-%d')
            to_date_str = to_date.strftime('%Y-%m-%d')
            user = self.request.user
            queryset = Transaction.objects.filter(author=user, date__range=(from_date_str, to_date_str))
            return queryset
        else:
            pass


class TransactionEdit(UpdateView):
    model = Transaction
    template_name = 'edit_transaction.html'
    fields = '__all__'
