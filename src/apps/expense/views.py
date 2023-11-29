from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Expense, ExpenseCategory, PlannedExpense, Bills, BillsCategory, Savings, BillsAccount
from  .utils import validate_data
from .serializers import ExpensesSerializer, ExpensesCategorySerializer, PlannedExpenseSerializer, BillsSerializer, BillsCategorySerializer, SavingsSerializer, BillsAccountSerializer


class CreateListExpenseView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        data=request.data
        category_id=data.get('category_id')

        validation_result=validate_data(data, category_id)
        if validation_result['status'] != 'success':
            return Response(validation_result, status=status.HTTP_400_BAD_REQUEST)
        
        category=validation_result['category']

        serializer=ExpensesSerializer(data=data)
        if serializer.is_valid():
            serializer.save(ctegory_id=category)   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def get(self,request):
        expense=Expense.objects.all()
        serializer=ExpensesSerializer(expense, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveExpenseView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            expense=Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return Response({'error':'Expense does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=ExpensesSerializer(expense)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        data=request.data
        expense=Expense.objects.get(pk=pk)
        serializer=ExpensesSerializer(expense, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        expense=Expense.objects.get(pk=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CreateListExpenseCategoryView(APIView):

    def post(self,request):
        if not request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
            return Response({'error': 'Authentication and a status of superuser is required'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer=ExpensesCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        queryset=ExpenseCategory.objects.all()
        serializer=ExpensesCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveExpensesCategoryView(APIView):

    def get(self,request,pk):
        try:
            category=ExpenseCategory.objects.get(pk=pk)
        except ExpenseCategory.DoesNotExist:
            return Response({'error':'Expense category does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=ExpensesCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        category=ExpenseCategory.objects.get(pk=pk)
        if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
            serializer=ExpensesCategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Permission denied. This action is only allowed for superusers.", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        category=ExpenseCategory.objects.get(pk=pk)
        if request.user.is_authenticated  and request.user_is_superuser and request.user.is_staff:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Permission denied. This action is only allowed for superusers.", status=status.HTTP_403_FORBIDDEN)
    

    
class PlannedExpenseView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        data=request.data
        target_date_str = data.get('target_date')

        try:
            target_date = datetime.strptime(target_date_str, "%Y-%m-%d")  
        except ValueError:
            return Response({'error': 'Invalid date format for target_date'}, status=status.HTTP_400_BAD_REQUEST)
        
        current_date = datetime.now()
        
        if target_date < current_date:
            return Response({'error': 'You can not point a previous date'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer=PlannedExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        planned_expenses=PlannedExpense.objects.all()
        serializer=PlannedExpenseSerializer(planned_expenses, many=True)
        return Response(serializer.data)


class RetrievePlannedExpenseView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            planned_expense=PlannedExpense.objects.get(pk=pk)
        except PlannedExpense.DoesNotExist:
            return Response({'error':'Planned expense does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=PlannedExpenseSerializer(planned_expense)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        planned_expense=PlannedExpense.objects.get(pk=pk)
        serializer=PlannedExpenseSerializer(planned_expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        planned_expense=PlannedExpense.objects.get(pk=pk)
        planned_expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BillsAccountView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        data=request.data
        serializer=BillsAccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        bill_account=BillsAccount.objects.all()
        serializer=BillsAccountSerializer(bill_account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveBillsAccountView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        bill=BillsAccount.objects.get(pk=pk)
        serializer=BillsAccountSerializer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        bill=BillsAccount.objects.get(pk=pk)
        serializer=BillsAccountSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)

    
    def delete(self,request,pk):
        bill=BillsAccount.objects.get(pk=pk)
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BillsCategoryView(APIView):

#     def post(self,request):
        
#         if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
#             serializer=BillsCategorySerializer({'error': 'Authentication and a status of superuser is required'}, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response("Permission denied. This action is only allowed for superusers.", status=status.HTTP_403_FORBIDDEN)
    
    def get(self, request):
        billscategory=BillsCategory.objects.all()
        serializer=BillsCategorySerializer(billscategory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class RetrieveBillsCategoryView(APIView):

    def get(self,request,pk):
        billscategory=BillsCategory.objects.get(pk=pk)
        serializer=BillsCategorySerializer(billscategory)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def put(self,request,pk):
    #     category=ExpenseCategory.objects.get(pk=pk)
    #     if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
    #         serializer=BillsCategorySerializer(category, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response("Permission denied. This action is only allowed for superusers.", status=status.HTTP_403_FORBIDDEN)

    
    # def delete(self,request,pk):
    #     category=BillsCategory.objects.get(pk=pk)
    #     if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
    #        category.delete()
    #        return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response("Permission denied. This action is only allowed for superusers.", status=status.HTTP_403_FORBIDDEN)


class SavingsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        target_date_str = data.get('target_date')
        
        try:
            target_date = datetime.strptime(target_date_str, "%Y-%m-%d")  
        except ValueError:
            return Response({'error': 'Invalid date format for target_date'}, status=status.HTTP_400_BAD_REQUEST)
        
        current_date = datetime.now()
        
        if target_date < current_date:
            return Response({'error': 'target_date cannot be in the past'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SavingsSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        savings = Savings.objects.all()
        serializer = SavingsSerializer(savings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RetrieveSavingsView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, pk):
        saving=Savings.objects.get(pk=pk)
        serializer=SavingsSerializer(saving)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        saving=Savings.objects.get(pk=pk)
        target_date=saving.target_date
        try:
            target_date = datetime.strptime(target_date, "%Y-%m-%d")
        except ValueError:
            return Response({'error': 'Invalid date format for target_date'}, status=status.HTTP_400_BAD_REQUEST)

        current_date=datetime.now() 

        if target_date and target_date < current_date:
            return Response({'error': 'target_date cannot be in the past'}, status=status.HTTP_400_BAD_REQUEST)
        
    
        serializer=SavingsSerializer(saving, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        saving=Savings.objects.get(pk=pk)
        saving.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

