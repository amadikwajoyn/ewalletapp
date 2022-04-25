import re
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .utils import Util


class UserCategory(models.Model):
    user_types = [('Noobs', 'Noobs'), ('Elite', 'Elite'), ]
    category = models.CharField(max_length=20, default=0, choices=user_types, primary_key=True)

    def __str__(self):
        return self.category


class Currency(models.Model):
    currency_types = [('USD', 'USD'), ('NGN', 'NGN'), ('BTC', 'BTC'), ]
    cur_category = models.CharField(max_length=20, default=0, choices=currency_types, primary_key=True)

    def __str__(self):
        return self.cur_category


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have an email')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    mobile = models.CharField(max_length=12, default=0, null=True)
    password = models.CharField(max_length=128, default=0, null=True)
    fullname = models.CharField(max_length=100, default=None, null=True)
    otp = models.CharField(max_length=10, default=None, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email


class UserAccountSetup(models.Model):
    user_id = models.ForeignKey(User, default=0, on_delete=CASCADE)
    user_types = models.ForeignKey(UserCategory, on_delete=CASCADE, null=True)
    currency_types = models.ForeignKey(Currency, default=None, on_delete=CASCADE, null=True)
    wallet_address = models.CharField(max_length=20, unique=True, primary_key=True)

    def generate_key(self):
        wallet_address = Util.generate_wallet_address()

        if UserAccountSetup.objects.filter(wallet_address=wallet_address).exists():
            return self.generate_key()

        return wallet_address

    def save(self, *args, **kwargs):
        if not self.wallet_address:
            self.wallet_address = self.generate_key()

        return super(UserAccountSetup, self).save(*args, **kwargs)

    def __str__(self):
        return self.wallet_address


class Transactions(models.Model):
    currency_types = models.ForeignKey(Currency, default=0, null=True, on_delete=CASCADE)
    wallet_address = models.ForeignKey(UserAccountSetup, default=0, on_delete=CASCADE)
    user_id = models.ForeignKey(User, default=0, null=True, on_delete=CASCADE)
    transaction_type = models.CharField(max_length=50, default=None)
    balance = models.DecimalField(max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class FundWallet(models.Model):
    user_id = models.ForeignKey(User, default=0, on_delete=CASCADE)
    currency_types = models.ForeignKey(Currency, default=0, on_delete=CASCADE)
    wallet_address = models.ForeignKey(UserAccountSetup, default=0, on_delete=CASCADE)
    amount = models.DecimalField(max_digits=50, decimal_places=2,  null=True, default=0)
    

class Balance(models.Model):
    wallet = models.ForeignKey(FundWallet, on_delete=CASCADE, null=True)
    balance = models.DecimalField(max_digits=50, decimal_places=2,  null=True, default=0)

  