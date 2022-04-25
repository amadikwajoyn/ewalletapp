from django.core.mail import EmailMessage
import random
from django.utils.crypto import get_random_string
from rest_framework import serializers
from django.contrib.auth import authenticate


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()

    @staticmethod
    def generate_otp():
        otp = random.randrange(100000, 1000000)
        return otp
    
    @staticmethod
    def generate_wallet_address():
        return get_random_string(19, allowed_chars='abcdefghijklmnopqrst_uvwxyz0123456789')
    
    


    # @staticmethod
# def get_and_authenticate_user(username, password):
#     user = authenticate(username=username, password=password)
#     if user is None:
#         raise serializers.ValidationError("Invalid username/password. Please try again!")
#     return user