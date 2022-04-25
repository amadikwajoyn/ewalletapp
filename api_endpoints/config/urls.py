"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from ewallet.views import FundWalletView
from ewallet.views import FundView, WithdrawalView, TransactionsView
schema_view = get_schema_view(
   openapi.Info(
      title="Ewallet App",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.walletapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@ewallet.com"),
      license=openapi.License(name="Wallet Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('fund/', FundWalletView.as_view(), name='fund'),
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/fund/<str:wallet_address>', FundView.as_view(), name='fund'),
    path('api/debit/<str:wallet_address>', WithdrawalView.as_view(), name='withdrawl'),
    path('api/transactions/<str:wallet_address>', TransactionsView.as_view(), name='transactions')
]
