from django.urls import path
from src.apps.income.views import IncomeView, RetrieveIncomeCategoryView, IncomeCategoryView, RetrieveIncomeView, PlannedIncomeView, RetrievePlannedIncomeView


urlpatterns=[
    path('income/post', IncomeView.as_view(), name='income_post'),
    path('income/retrieve/<int:pk>', RetrieveIncomeView.as_view(), name='income_retrieve'),
    path('income_category/post', IncomeCategoryView.as_view(), name='income_category'),
    path('income_category/retrieve/<int:pk>', RetrieveIncomeCategoryView.as_view(), name='income_category_retrieve'),
    path('planned_income/post', PlannedIncomeView.as_view(), name='planned_income_post'),
    path('planned_income/retrieve/<int:pk>', RetrievePlannedIncomeView.as_view(), name='planned_income_retrieve')
]

