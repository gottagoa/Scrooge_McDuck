from django.db import models
from datetime import date
from djmoney.models.fields import MoneyField

from src.apps.expense.models import Bills, BillsCategory, BillsAccount


class IncomeCategory(models.Model):
    name=models.CharField('Title', max_length=200)
    description=models.CharField('Description', max_length=200, blank=True)
    parent=models.ForeignKey("self", 
        on_delete=models.CASCADE, 
        related_name="subcategories",
        null=True,
        blank=True
    )
    image=models.ImageField('Icon', blank=True, upload_to='incomes/')

    class Meta: 
            verbose_name = "IncomeCategory"
            verbose_name_plural = "IncomeCategories"
        
    def __str__(self):
        return self.name


class Income(models.Model):
    PAYMENT_CHOICES= [
        ('Cash', 'Cash'),
        ('Non-cash', 'Non-cash'),
    ]
    name=models.CharField('Title', max_length=200, blank=True)
    amount=MoneyField(decimal_places=2, default_currency='KGS', max_digits=10)
    date=models.DateTimeField('Date', auto_now_add=True)
    description=models.CharField('Description', blank=True)
    category_id=models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='incomecategory')
    cash_income=models.CharField('Cash income', max_length=20, choices=PAYMENT_CHOICES, default='Cash')
    bill_account= models.ForeignKey(BillsAccount, null=True, blank=True, on_delete=models.CASCADE, related_name='incomes')
    class Meta:
            verbose_name='Income'
            verbose_name_plural='Incomes'

    def __str__(self):
        return f'You recieved {self.amount}'


class PlannedIncome(models.Model):
    name=models.CharField('Title', max_length=200)
    amount=MoneyField(decimal_places=2, default_currency='KGS', max_digits=10)
    date=models.DateTimeField('Date', auto_now_add=True, null=True, blank=True)
    
    class Meta:
            verbose_name='PlannedIncome'
            verbose_name_plural='PlannedIncomes'

    def __str__(self):
        return f'Planned income is {self.amount}'
     