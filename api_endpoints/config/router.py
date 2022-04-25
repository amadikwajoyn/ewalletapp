# from api_endpoints.ewallet.models import FundWallet
# from api_endpoints.ewallet.viewset import BalanceView
from ewallet.viewset import UserViewSet, LoginViewSet, UserCategoryViewSet, CurrencyViewSet, LogoutViewSet,\
                            UpdateUserViewSet, UserAccountSetupViewSet, UserVerifyViewSet
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register('register', UserViewSet, basename="register")
router.register('verify_user/', UserVerifyViewSet)
router.register('login', LoginViewSet, basename="login")
router.register('user_type', UserCategoryViewSet)
router.register('currency', CurrencyViewSet)
router.register('logout', LogoutViewSet)
router.register('update_users', UpdateUserViewSet)
router.register('user_setup', UserAccountSetupViewSet)


