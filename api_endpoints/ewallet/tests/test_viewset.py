from django.test import TestCase
# from rest_framework.test import APITestCase
# from .models import Users
# import django_heroku

from .test_setup import TestSetup
from ..models import User

class TestViews(TestSetup):
    def test_user_cannot_register_with_no_data(self):
        res= self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res= self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)

    def test_user_register_data(self):
        res= self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)

    def test_user_can_login_after_verified(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()

        ress = self.client.post(self.login_url, self.user_data, format="json" )
        self.assertEqual(ress.status_code, 200)
    
    # def test_user_detail(self):
    #     self.client.force_authenticate(user=self.user_data)
    #     response = self.client.post(self.user_detail_url, {'pk': self.user_data.id }, format='json')
