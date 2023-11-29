from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from .models import Expense, ExpenseCategory, PlannedExpense,Bills,BillsCategory,Savings, BillsAccount, Wallet
# Register your models here.
from .form import ExpenseAdminForm



@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'payment_method', 'bill_account')
    form = ExpenseAdminForm


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(PlannedExpense)
admin.site.register(Bills)
admin.site.register(BillsCategory)
admin.site.register(Savings)
admin.register(BillsAccount)
admin.site.register(Wallet)



