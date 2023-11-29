from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Income, IncomeCategory, PlannedIncome
from .serializers import IncomeSerializer, IncomeCategorySerializer, PlannedIncomeSerializer


class IncomeView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        data=request.data
        serializer=IncomeSerializer(data=data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        income=Income.objects.all()
        serializer=IncomeSerializer(income, many=True)
        return Response(serializer.data)



class RetrieveIncomeView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            income= Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            return Response({'error':'Income does not exist'})
        
        serializer=IncomeSerializer.objects(income)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        data=request.data
        income=Income.objects.get(pk=pk)
        serializer=IncomeSerializer(income, data=data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        income=Income.objects.get(pk=pk)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class IncomeCategoryView(APIView):
    def post(self, request):
        data=request.data
        if not request.user.is_authentificated and request.user.is_staff and request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer=IncomeCategorySerializer(data=data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        category=IncomeCategory.objects.all()
        serializer=IncomeCategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RetrieveIncomeCategoryView(APIView):
    def get(self,request,pk):
        try:
            income_category=IncomeCategory.objects.get(pk=pk)
        except IncomeCategory.DoesNotExist:
            return Response({'errors: IncomeCategory does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer=IncomeCategorySerializer(income_category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        income_category=IncomeCategory.objects.get(pk=pk)
        data=request.data
        if not request.user.is_authentificated and request.user.is_staff and request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer=IncomeCategorySerializer(income_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if not request.user.is_authentificated and request.user.is_staff and request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        income_category=IncomeCategory.objects.get(pk=pk)
        income_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

class PlannedIncomeView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        data=request.data
        serializer=PlannedIncomeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        planned_incomes=PlannedIncome.objects.all()
        serializer=PlannedIncomeSerializer(planned_incomes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


class RetrievePlannedIncomeView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, pk):
        planned_income=PlannedIncome.objects.get(pk=pk)
        serializer=PlannedIncomeSerializer(planned_income)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        planned_income=PlannedIncome.objects.get(pk=pk)
        serializer=PlannedIncomeSerializer(planned_income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        planned_income=PlannedIncome.objects.get(pk=pk)
        planned_income.delete()
        return Response(status=status.HTTP_200_OK)


