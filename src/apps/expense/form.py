from django.http import request
from django.shortcuts import render
from django import forms
from .models import Expense

class ExpenseAdminForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        payment_method = self.initial.get('payment_method') or self.data.get('payment_method')
        if payment_method == 'Cash':
            self.fields['bill_account'].queryset = Expense._meta.get_field('bill_account').related_model.objects.none()
