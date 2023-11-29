from rest_framework import serializers
from src.apps.expense.models import Bills, Expense, BillsAccount, PlannedExpense, ExpenseCategory, BillsCategory, Savings
from rest_framework.response import Response
from rest_framework import status

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bills
        exclude=['id']


class BillsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BillsCategory
        exclude=['id']


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        exclude=['id']
        
    def validate(self, data):
        if data['payment_method']=='Cash':
            if data.get("bill_account") is not None or data.get("wallet") is None:
                raise serializers.ValidationError({'payment_method':'You can not choose this option'})
            if data['wallet'].amount.amount < data['amount']:
                raise serializers.ValidationError({'message': 'You do not have money'}) 
        else:
            if data.get("bill_account") is None or data.get("wallet") is not None:
                raise serializers.ValidationError({'payment_method':'There is no any bill accounts'})
            if data['bill_account'].amount.amount < data['amount']:
                raise serializers.ValidationError({'message': 'You do not have money'})
    
        return data


class ExpensesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseCategory
        exclude=['id']
        

class PlannedExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlannedExpense
        exclude=['id']

class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Savings
        exclude=['id', 'date']

class BillsAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillsAccount
        exclude=['id']
