from django.urls import path
from .views import CreateListExpenseCategoryView, CreateListExpenseView, PlannedExpenseView, RetrieveExpenseView, RetrievePlannedExpenseView, RetrieveExpensesCategoryView, BillsAccountView, RetrieveBillsAccountView, BillsCategoryView, RetrieveBillsCategoryView, SavingsView, RetrieveSavingsView

urlpatterns=[
    path('expenses/post/', CreateListExpenseView.as_view(), name='list_expenses'),
    path('expenses/retrieve/<int:pk>', RetrieveExpenseView.as_view(), name='retrieve_expenses'),
    path('expenses_categories/post/', CreateListExpenseCategoryView.as_view(), name='list_create_categories'),
    path('expenses_categories/retrieve/<int:pk>', RetrieveExpensesCategoryView.as_view(), name='retrieve_expenses_category'),
    path('planned_expenses/post/', PlannedExpenseView.as_view(), name='planned_expense'),
    path('planned_expenses/retrieve/<int:pk>',RetrievePlannedExpenseView.as_view(), name='retrieve_planned_expenses'),
    path('bills/post/', BillsAccountView.as_view(), name='bills_post'),
    path('bills/retrieve/<int:pk>', RetrieveBillsAccountView.as_view(), name='retrieve_bills'),
    path('bills_categories/post/', BillsCategoryView.as_view(), name='bills_category_post'),
    path('retrieve_bills_category/<int:pk>', RetrieveBillsCategoryView.as_view(), name='retrieve_bills_category'),
    path('savings/post/', SavingsView.as_view(), name='savings_post'),
    path('savings/retrieve/<int:pk>', RetrieveSavingsView.as_view(), name='savings_retrieve')
]