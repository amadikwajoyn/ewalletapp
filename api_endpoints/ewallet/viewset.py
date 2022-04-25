from urllib import request
from rest_framework import viewsets, generics
from django.db import models
from rest_framework import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import logout
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from .serializers import *
from . import models
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UsersSerializers
    permission_classes = [AllowAny]
    http_method_names = ['post',  'head']
    
    def create(self, request):
        serializers = UsersSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            user_data = serializers.data
            user = User.objects.get(email = user_data['email'])
            
            otp = Util.generate_otp()
            user.otp = otp
            print(otp)
            user.save()
            current_site = get_current_site(request).domain

            urlsget = 'http://'+current_site+'?token='+str(otp)
            email_body = f"This is your OTP code: {otp}"
            data = {
                'email_body': email_body + urlsget,
                'to_email':user.email,
                'email_subject': 'Verify your Email'
            }
            Util.send_email(data)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerifyViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserVerifySerializer
    permission_classes = [AllowAny]
    http_method_names = ['post', 'head']

    def create(self, request):
        data = request.data
        otp = data.get('otp', '')
        email = data.get('email', '')
        if otp is None or email is None:
            return Response(errors=dict(invalid_input="OTP and/or email needed"), status=status.HTTP_400_BAD_REQUEST)
        get_user = User.objects.filter(email=email)
        if not get_user.exists():
            return Response(errors=dict(invalid_email = "Provided email is not registered"), status=status.HTTP_400_BAD_REQUEST )
        user = get_user[0] 
        if user.otp != otp:
            return Response(errors=dict(invalid_otp = "Please provide a valid otp code"), status=status.HTTP_400_BAD_REQUEST)
        user.is_verified = True
        user.save()
        return Response(data={
                "verified status":"Congrats, your account have been successfully verified"
            }, status=status.HTTP_200_OK)


class LoginViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post', 'head']

    def create(self, request, *args, **kwargs):
        # user_id = User.objects.filter(id=pk)
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if User.is_verified == False:
            pass
        else:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)


class UserAccountSetupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.UserAccountSetup.objects.all()
    serializer_class = UserAccountSetupSerializers
    if not permission_classes:
        http_method_names = ['get', 'head']


class UpdateUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.User.objects.all()
    serializer_class = UpdateUserSerializers


class UserCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.UserCategory.objects.all()
    serializer_class = UserCategorySerializers


class CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.Currency.objects.all()
    serializer_class = CurrencySerializers

class FundBalanceViewSet(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = models.Balance.objects.all()
    serializer_class = BalanceSerializers
    http_method_names = ['post','get','put', 'head']

    # def get_queryset(self):
    #     queryset = FundWallet.objects.filter(id = request.wallet_address)

# class FundWalletViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = models.FundWallet.objects.all()
#     serializer_class = FundWalletSerializers
#     http_method_names = ['post','get', 'put', 'head']


# class WithdrawFundsViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = models.FundWallet.objects.all()
#     serializer_class = WithdrawFundsSerializers
#     http_method_names = ['get', 'put', 'head']

#     if not permission_classes:
#         http_method_names = ['get', 'head']


class LogoutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.User.objects.all()
    serializer_class = UserLogoutSerializer
    http_method_names = ['get', 'head']

    def get(self):
        logout(self)
        return Response(status=status.HTTP_200_OK)






