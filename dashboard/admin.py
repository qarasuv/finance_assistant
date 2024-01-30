from django.contrib import admin

from .models import Transaction, TransactionCategory


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'amount', 'description', 'category', 'author')
