from django.db import models
from django.utils import timezone
from users.models import User


class TransactionCategory(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(User, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    type = models.CharField(max_length=16)
    date = models.DateField(default=timezone.now)
    amount = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(TransactionCategory, related_name='transaction', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return f'/transactions/history'


