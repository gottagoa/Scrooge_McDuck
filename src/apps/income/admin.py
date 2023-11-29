from django.contrib import admin
from .models import Income, IncomeCategory, PlannedIncome

# Register your models here.
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(IncomeCategory)
admin.site.register(PlannedIncome)