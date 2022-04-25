from posixpath import basename
from webbrowser import get
from .models import (Balance, User, UserAccountSetup, UserCategory, Currency, FundWallet, Transactions)
from django.contrib.auth import authenticate
from rest_framework import serializers


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']

    def validate_username(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User not found')
        
        return email

    def validate(self, data):
        # authentications
        request = self.context.get('request')
        email = data.get('email')  # test_name
        password = data.get('password')  # new password11
        get_user = User.objects.filter(email=email)
        user1 = get_user[0] 
        if email and password:
            print('user entered password', password)
            print(User.objects.get(email=email))
            user = authenticate(email=email, password=password, request=request)
            if not user:
                raise serializers.ValidationError('Invalid password')
            if user1.is_verified == False:
                raise serializers.ValidationError('User is not verified')
        else:
            raise serializers.ValidationError('You have to type your email and password')
        data['user'] = user
        return data

class UserVerifySerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['otp', 'email']


class UserLogoutSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['username', 'password']
    

class UpdateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'mobile', 'fullname']
    
        def update(self, instance, validated_data):
            instance.mobile = validated_data.get('mobile', instance.mobile)
            instance.fullname = validated_data.get('fullname', instance.fullname)
            instance.save()
            return instance


class UpdateCurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'currency_types']
    
    def update(self, instance, validated_data):
        instance.currency_types = validated_data.get('currency_types', instance.currency_types)
        instance.save()
        return instance


class UserAccountSetupSerializers(serializers.ModelSerializer):
    wallet_address = serializers.ReadOnlyField()
    class Meta:
        model = UserAccountSetup
        fields = '__all__'
        # exclude= ('wallet_address',)
    
    def validate(self, attrs):
        user_id = attrs.get('email', '')
        user_types = attrs.get('user_types', '')
        currency_types = attrs.get('currency_types', '')
        if UserAccountSetup.objects.filter(user_types= 'Elite').exists():  # for elite users
            if UserAccountSetup.objects.filter(currency_types=currency_types).filter(user_id=user_id)\
                    .filter(user_types=user_types).exists():
                raise serializers.ValidationError(
                    {'User': 'Currency already exist'})
            return super().validate(attrs)
            
        if UserAccountSetup.objects.filter(user_types = 'Noobs').exists():  # for noobs users
            if UserAccountSetup.objects.filter(user_id=user_id).filter(user_types=user_types).exists():
                raise serializers.ValidationError(
                    {'User': 'You are not allowed to Update you current'})
            return super().validate(attrs)
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.user_types = validated_data.get('user_types', instance.user_types)
        instance.currency_types = validated_data.get('currency_types', instance.currency_types)
        instance.save()
        return instance
        

class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['otp', 'email']


class UserCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = ('category',)


class CurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('cur_category',)


class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['user_id', 'wallet_address', 'currency_types', 'balance', 'transaction_type', 'created_at']
        # exclude = ('id',)
     

class BalanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'


class FundWalletSerializers(serializers.ModelSerializer):
    class Meta:
        model = FundWallet
        fields = ['user_id', 'wallet_address', 'currency_types', 'amount']
    
    def validate(self, attrs):
        wallet_address= attrs.get('wallet_address', '')
        currency_types= attrs.get('currency_types', '')
        if UserAccountSetup.objects.filter(wallet_address = wallet_address).exists():  # for elite users
            if not UserAccountSetup.objects.filter(currency_types=currency_types).filter(wallet_address=wallet_address).exists():
                raise serializers.ValidationError(
                    {'Ewallet': 'Invalid credentials'})
            return super().validate(attrs)


class WithdrawFundsSerializers(serializers.ModelSerializer):
    class Meta:
        model = FundWallet
        fields = ['user_id', 'wallet_address', 'currency_types', 'amount']
        # exclude = ('balance',)
    
    def validate(self, attrs):
        wallet_address= attrs.get('wallet_address', '')
        currency_types= attrs.get('currency_types', '')
        # amount= attrs.get('amount', '')
        if UserAccountSetup.objects.filter(wallet_address = wallet_address).exists():  # for elite users
            if not UserAccountSetup.objects.filter(currency_types=currency_types).filter(wallet_address=wallet_address).exists():
                raise serializers.ValidationError(
                    {'Ewallet': 'Invalid credentials'})
            return super().validate(attrs)
