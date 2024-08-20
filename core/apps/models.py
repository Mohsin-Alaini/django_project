from django.db import models
from django.db.models import Sum
# Create your models here.

class Currency(models.Model):
    code = models.CharField(verbose_name='رمز العملة', max_length=15)
    name = models.CharField(verbose_name='اسم العملة', max_length=50)
    local = models.BooleanField(verbose_name='عملة محلية', default=False)
    
    def __str__(self):
        return self.code
    
class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    exchange_rate = models.FloatField(verbose_name='سعر الصرف')
    max_exchange_rate = models.FloatField(verbose_name='اعلى سعر صرف')
    min_exchange_rate = models.FloatField(verbose_name='ادتى سعر صرف')
    date = models.DateTimeField( auto_now_add=True)
    def __str__(self) -> str:
        return str(self.date) + ' -    '+str(self.currency)+ ' - ' + str(self.exchange_rate)

class AccountType(models.Model):
    name = models.CharField(verbose_name='نوع الحساب', max_length=50)
    description = models.CharField(verbose_name='الوصف', max_length=200)
    def __str__(self):
        return self.name
    
class Account(models.Model):
    STATUS_CHOICES = [
        (1, 'نشط'),
        (2, 'موقف'),
    ]
    number = models.CharField(verbose_name='رقم الحساب', max_length=15, blank=False, null=False)
    name = models.CharField(verbose_name='اسم الحساب', max_length=100, blank=False, null=False)
    status = models.IntegerField(verbose_name='الحالة', choices=STATUS_CHOICES, blank=False, null=False)
    type = models.ForeignKey(AccountType, verbose_name='نوع الحساب', on_delete=models.CASCADE)
    currency = models.ManyToManyField(Currency, verbose_name='العملات')
    def __str__(self):
        return self.name 
    
    def balance(self):
        balance = TransactionDetails.objects.filter(account__id=self.id).aggregate(balance=Sum('debit') - Sum('credit'))
        return balance['balance']
            
class Transaction(models.Model):
    number = models.CharField(verbose_name='رقم العملية', max_length=15)
    date = models.DateField(verbose_name='التاريخ')
    def __str__(self):
        return self.number + ' - ' + str(self.date)
    
    
class TransactionDetails(models.Model):
    account = models.ForeignKey(Account, verbose_name='الحساب', on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, verbose_name='العملة', on_delete=models.CASCADE)
    exchang_rate = models.FloatField(verbose_name='سعر التحويل')
    debit = models.FloatField(verbose_name='المبلغ المدين', blank=True, null=True,default=0)
    credit = models.FloatField(verbose_name='المبلغ الدائن', blank=True, null=True,default=0)
    note = models.TextField(verbose_name='ملاحظة', max_length=300)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
     