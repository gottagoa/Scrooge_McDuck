from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer, UserUpdateSerializer


class UserRegistrationView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():
            user=serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'message':'User was succesfully created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(RetrieveUpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=UserUpdateSerializer

    def get_object(self):
        return self.request.user

class ChangePasswordView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        form=PasswordChangeForm(user=request.user, data=request.data)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return Response({'message':'The password has been succesfully changed'}, status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


           






            


