from rest_framework.response import Response
from rest_framework import serializers, viewsets, status
from src.apps.expense.models import Bills, BillsCategory, Expense, ExpenseCategory


def validate_data(data, category_id):
    if category_id is None:
        return {'status': 'error', 'error': 'Category ID not provided'}
    try:
        category = ExpenseCategory.objects.get(pk=category_id)
        return {'status': 'success', 'category': category}
    except ExpenseCategory.DoesNotExist:
        return {'status': 'error', 'error': 'Category not found'}
    
