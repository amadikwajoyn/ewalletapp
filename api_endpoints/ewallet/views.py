# from django.shortcuts import render
from locale import currency
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


class FundView(generics.GenericAPIView):
        serializer_class = FundWalletSerializers
        permission_classes = [IsAuthenticated]
        def post(self, request, wallet_address):
            print(request.data)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = models.UserAccountSetup.objects.get(wallet_address=wallet_address)
            transaction_type = 'Credit'
            balance = FundWallet.objects.filter(wallet_address=user).first()
            if balance:
                credit_or_debit = serializer.validated_data.get('amount')
                balance.amount += credit_or_debit
                balance.save()

                # updating the transaction model 
                account = UserAccountSetup.objects.get(wallet_address = user)
                transaction = Transactions.objects.create(
                    user_id = account.user_id,
                    wallet_address= user,
                    currency_types = account.currency_types,
                    transaction_type = transaction_type,
                    balance = credit_or_debit
                )
                transaction.save()
                return Response({"success": f'account funded sucessfully with {credit_or_debit}'}, status=status.HTTP_201_CREATED)
            else:
                account = UserAccountSetup.objects.get(wallet_address = user)
                balance = FundWallet.objects.create(
                    wallet_address = user,
                    user_id = account.user_id,
                    currency_types = account.currency_types,
                    amount = 0
                )
                credit_or_debit = serializer.validated_data.get('amount')
                balance.amount += credit_or_debit
                balance.save()

                # update transaction model 
                account = UserAccountSetup.objects.get(wallet_address = user)
                transaction = Transactions.objects.create(
                    user_id = account.user_id,
                    wallet_address= user,
                    currency_types = account.currency_types,
                    transaction_type = transaction_type,
                    balance = credit_or_debit
                )
                transaction.save()
                return Response({"success": f'account funded sucessfully with {credit_or_debit}'}, status=status.HTTP_201_CREATED)
            

class WithdrawalView(generics.GenericAPIView):
    serializer_class = FundWalletSerializers
    permission_classes = [[IsAuthenticated]]
    def post(self, request, wallet_address):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = models.UserAccountSetup.objects.get(wallet_address=wallet_address)
        transaction_type = 'Debit'
        balance = FundWallet.objects.filter(wallet_address=user).first()
        if balance:
            credit_or_debit = serializer.validated_data.get('amount')
            if balance.amount >= credit_or_debit:
                balance.amount -= credit_or_debit
                balance.save()

                # update the transaction model
                account = UserAccountSetup.objects.get(wallet_address = user)
                transaction = Transactions.objects.create(
                    user_id = account.user_id,
                    wallet_address= user,
                    currency_types = account.currency_types,
                    transaction_type = transaction_type,
                    balance = credit_or_debit
                )
                transaction.save()

                return Response({"success": f'account debited sucessfully with {credit_or_debit}'}, status=status.HTTP_201_CREATED)
            else:
                balance.amount = balance.amount
                balance.save()
                return Response({'Error': f'Insuffient funds. Your account balance is {balance.amount}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            account = UserAccountSetup.objects.get(wallet_address = user)
            balance = FundWallet.objects.create(
                wallet_address = user,
                user_id = account.user_id,
                currency_types = account.currency_types,
                amount = 0
            )
            credit_or_debit = serializer.validated_data.get('amount')
            balance.amount -= credit_or_debit
            balance.save()
            
            # updating the transaction model 
            account = UserAccountSetup.objects.get(wallet_address = user)
            transaction = Transactions.objects.create(
                user_id = account.user_id,
                wallet_address= user,
                currency_types = account.currency_types,
                transaction_type = transaction_type,
                balance = credit_or_debit
            )
            transaction.save()
            return Response({"Error": f'Insufficient fund, kindly credit your account'}, status=status.HTTP_402_PAYMENT_REQUIRED)


class TransactionsView(generics.GenericAPIView):
    serializer_class = TransactionsSerializers
    permission_classes = [[IsAuthenticated]]

    def get(self,request, wallet_address):
        user = models.UserAccountSetup.objects.get(wallet_address = wallet_address)
        queryset = models.Transactions.objects.filter(wallet_address = user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# class BalView(generics.GenericAPIView):
#     serializer_class = FundWalletSerializers
#     permission_classes = (AllowAny,)
#     # queryset = FundWallet.objects.all()

#     def get(self, request, wallet_address):
#         user = models.UserAccountSetup.objects.get(wallet_address=wallet_address)
#         queryset = models.FundWallet.objects.filter(wallet_address=user)
#         serializer = self.serializer_class(queryset, many=True)
#         user_record_orderdict = serializer.data
#         amount_list = [ i['amount'] for i in user_record_orderdict ]
#         amount_list_convertion  = list(map(float, amount_list))
#         balance = sum(amount_list_convertion)

        # return Response(f'balance for {wallet_address} : {balance}', status=status.HTTP_200_OK)
