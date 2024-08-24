from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q , Max , Min , Avg ,Sum, F
from ..models import Currency,ExchangeRate,Account,TransactionDetails,Transaction
from .forms import InfonForm,CurrencyForm
# Create your views here.
def view(request):
    # Currency.objects.create(code = 'YER',name = "Yemeni",local= True)
    # cur = Currency.objects.all().first()
    # ExchangeRate.objects.create(currency=cur, exchange_rate=1,max_exchange_rate=1,min_exchange_rate=1)
    # print(cur,'pppppppppppp')    
    # exchangeRate = ExchangeRate.objects.values('exchange_rate','currency__name')
    # currency = Currency.objects.values('id','name','exchangerate__exchange_rate')
    # clint_trans = Account.objects.filter(name='client2').values('name','transactiondetails__debit','transactiondetails__credit')     
    # transactions = TransactionDetails.objects.filter(~Q(account__number='1',transaction__date__gte='2024-05-10',account__name='client1')).aggregate(sum_debit=Sum('debit'),sum_credit=Sum('credit'))
    # transactions = TransactionDetails.objects.values('account__name','currency__name').annotate(sum_debit=Sum('debit'),sum_credit=Sum('credit')).annotate(balance=F('sum_debit')-F('sum_credit'))
    
    # print('----------')
    # print(transactions)
    # print('----------') 
    # for cu in transactions:
    #     print(cu) 
    
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            currency = form.save(commit=False)
            currency.local = False
            currency.save()
            # print(form.cleaned_data['number'],'view')
        else:
            print(form.errors)
    else :
        form = CurrencyForm()
    context = {
        'form':form,
        # 'transactions' : transactions,
        # 'currency':currency
    }
    return render(request , 'account_page.html',context)


def view2(request,id):
    return HttpResponse('view2')
def view3(request,id,name):
    return HttpResponse('view3')