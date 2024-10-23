from django.forms import ModelForm

from .models import TransactionCategory, Transaction


class TransactionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TransactionForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['category'].queryset = TransactionCategory.objects.filter(author=user)

    class Meta:
        model = Transaction
        fields = ['type', 'date', 'amount', 'description', 'category', 'author']


class TransactionCategoryForm(ModelForm):
    class Meta:
        model = TransactionCategory
        exclude = '__all__'