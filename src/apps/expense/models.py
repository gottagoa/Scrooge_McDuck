from django.db import models
import django.db.models.deletion
import django.utils.timezone
from djmoney.models.fields import MoneyField
from src.apps.account.models import User


class BillsCategory(models.Model):

    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Non-cash', 'Non-cash'),
    ]
    
    payment_method = models.CharField('Payment Method', max_length=100, choices=PAYMENT_CHOICES, default='Other')
    description = models.CharField('Description', blank=True, max_length=200)
    
    class Meta:
        verbose_name = 'BillCategory'
        verbose_name_plural = 'BillCategories'

    def __str__(self):
        return self.payment_method


class Bills(models.Model):
    name = models.CharField('Bank', max_length=200, unique=True)
    category = models.ForeignKey(BillsCategory, on_delete=models.CASCADE, related_name='bills', limit_choices_to={'payment_method': 'Non-cash'})

    class Meta():
        verbose_name='Bills'
        verbose_name_plural='Bills'

    def __str__(self):
        return self.name
    

class BillsAccount(models.Model):
    name=models.CharField('Account', max_length=20, unique=True)
    amount=MoneyField(decimal_places=2, default_currency='KGS', max_digits=10)
    bank=models.ForeignKey(Bills, on_delete=models.CASCADE, related_name='billsaccount')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='bills_accounts')

    class Meta():
        verbose_name='BillsAccount'
        verbose_name_plural='BillsAccounts'

    def __str__(self):
        return self.name


class Wallet(models.Model):
    name=models.CharField('Wallet', max_length=100, unique=True)
    amount=MoneyField(decimal_places=2, default_currency='KGS', max_digits=10)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallets')

    class Meta():
        verbose_name='Wallet'
        verbose_name_plural='Wallets'

    def __str__(self):
        return self.name


class ExpenseCategory(models.Model):
    name=models.CharField('Title', max_length=200, unique=True, blank=True)
    description=models.CharField(max_length=300, verbose_name='Description', blank=True)
    parent=models.ForeignKey("self", 
        on_delete=models.CASCADE, 
        related_name="subcategories",
        null=True,
        blank=True)
    
    class Meta():
        verbose_name='ExpenseCategory'
        verbose_name_plural='ExpenseCategories'

    def __str__(self):
        return self.name



class Savings(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='savings')
    name=models.CharField('Title', max_length=200)
    description=models.CharField('Description', max_length=300, null=True, blank=True)
    amount=MoneyField(decimal_places=2, default_currency='KGS', max_digits=10)
    date=models.DateTimeField('Date', auto_now_add=True)
    target_date=models.DateTimeField('Date', auto_now_add=True)

    class Meta():
        verbose_name='Savings'
        verbose_name_plural='Savings'

    def __str__(self):
        return self.name


class PlannedExpense(models.Model):
    name=models.CharField('Title', max_length=300)
    date=models.DateField('Date', auto_now_add=True)
    amount=MoneyField('Amount', decimal_places=2, default_currency='KGS', max_digits=10)          
    category_id=models.ForeignKey(ExpenseCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='plannedexpenses')

    class Meta():
        verbose_name='PlannedIncome'
        verbose_name_plural='PlannedIncomes'
    
    def __str__(self):
        return self.name


class Expense(models.Model):
    PAYMENT_CHOICES= [
        ('Cash', 'Cash'),
        ('Non-cash', 'Non-cash'),
    ]
    
    name=models.CharField('Title', max_length=300)
    date=models.DateTimeField('Date', auto_now_add=True)
    description = models.CharField('Description', null=True, blank=True, max_length=300)
    amount=MoneyField(decimal_places=2, default_currency='KGS', max_digits=10)
    payment_method = models.CharField('Payment Method', max_length=20, choices=PAYMENT_CHOICES, default='Cash')
    wallet=models.ForeignKey(Wallet, null=True, blank=True, on_delete=models.CASCADE, related_name='expenses')
    bill_account= models.ForeignKey(BillsAccount, null=True, blank=True, on_delete=models.CASCADE, related_name='expenses') #limit_choices_to={'category__payment_method': 'Non-cash'}
    ctegory_id=models.ForeignKey(ExpenseCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='expensescategory')  

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
    
    def __str__(self):
        return self.name
      


