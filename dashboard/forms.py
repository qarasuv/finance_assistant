from django.forms import ModelForm

from .models import *


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = '__all__'