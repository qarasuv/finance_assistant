from datetime import datetime

from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import openpyxl

from .forms import *


class Index(ListView):
    model = TransactionCategory
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return TransactionCategory.objects.filter(author=self.request.user.id)


class TransactionAdd(CreateView):
    form_class = TransactionForm
    template_name = 'add_transaction.html'
    success_url = reverse_lazy('index')


class CategoryAdd(CreateView):
    form_class = TransactionCategoryForm
    template_name = 'add_category.html'
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

    def get_queryset(self):
        date_range = self.request.GET.get('date_range')
        if date_range:
            from_date, to_date = map(lambda x: datetime.strptime(x.strip(), '%m/%d/%Y'), date_range.split('-'))
            return Transaction.objects.filter(author=self.request.user, date__range=(from_date, to_date))


class Category(ListView):
    model = Transaction
    template_name = 'category_detail.html'
    context_object_name = 'transactions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = TransactionCategory.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        return Transaction.objects.filter(author=self.request.user.id, category__pk=self.kwargs.get('pk'))


class TransactionEdit(UpdateView):
    model = Transaction
    template_name = 'edit_transaction.html'
    fields = '__all__'


class ReportExport(ListView):
    template_name = 'report.html'
    context_object_name = 'report_data'
    model = Transaction

    def get_queryset(self):
        date_range = self.request.GET.get('date_range')
        if date_range:
            from_date, to_date = map(lambda x: datetime.strptime(x.strip(), '%m/%d/%Y'), date_range.split('-'))
            return Transaction.objects.filter(author=self.request.user, date__range=(from_date, to_date))

    def get(self, request, *args, **kwargs):
        report_data = self.get_queryset()
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.append(['Type', 'Date', 'Amount', 'Category', 'Description'])

        for transaction in report_data:
            worksheet.append([str(transaction.type), str(transaction.date), str(transaction.amount),
                              str(transaction.category), str(transaction.description)])

        workbook.save(response)
        return response
