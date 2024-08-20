from django.shortcuts import render
from django.http import HttpResponse
from ..models import Currency,ExchangeRate
# Create your views here.
def view(request):
    # Currency.objects.create(code = 'YER',name = "Yemeni",local= True)
    # cur = Currency.objects.all().first()
    # ExchangeRate.objects.create(currency=cur, exchange_rate=1,max_exchange_rate=1,min_exchange_rate=1)
    # print(cur,'pppppppppppp')    
    exchangeRate = ExchangeRate.objects.values('exchange_rate','currency__name')
    currency = Currency.objects.values('id','name','exchangerate__exchange_rate')
    
    for cu in currency:
        print(cu)    
    return HttpResponse('view1')


def view2(request,id):
    return HttpResponse('view2')
def view3(request,id,name):
    return HttpResponse('view3')