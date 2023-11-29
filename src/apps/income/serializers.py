from rest_framework import serializers
from src.apps.income.models import Income, IncomeCategory,  PlannedIncome

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Income
        exclude=['id']

class IncomeCategorySerializer(serializers.ModelSerializer):
     class Meta:
        model=IncomeCategory
        exclude=['id']

class PlannedIncomeSerializer(serializers.ModelSerializer):
     class Meta:
        model=PlannedIncome
        exclude=['id']