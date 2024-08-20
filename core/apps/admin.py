from django.contrib import admin
from .models import Account,AccountType,Currency,ExchangeRate,Transaction,TransactionDetails
# Register your models here.

admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(Currency)
admin.site.register(Transaction)
admin.site.register(TransactionDetails)
admin.site.register(ExchangeRate)