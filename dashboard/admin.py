from django.contrib import admin

from .models import *


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'amount', 'description', 'category', 'user')
