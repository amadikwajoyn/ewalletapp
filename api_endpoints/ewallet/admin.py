from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(User)
admin.site.register(UserCategory)
admin.site.register(Currency)
admin.site.register(UserAccountSetup)
admin.site.register(Transactions)
admin.site.register(FundWallet)
admin.site.register(Balance)