from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from ..models import User
from ..viewset import UserViewSet
class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register-list')
        self.login_url = reverse('login-list')
        # self.user_detail_url= reverse('user-detail')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),

        }

        return super().setUp()
    
    def tearDown(self) -> None:

        return super().tearDown()

