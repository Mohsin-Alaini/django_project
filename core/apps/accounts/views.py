from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q , Max , Min , Avg ,Sum, F
from ..models import Currency,ExchangeRate,Account,TransactionDetails,Transaction,AccountType
from .forms import AccountTypeForm, InfonForm,CurrencyForm
from django.views import View
from django.urls import reverse
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

# Class-Base-View
class AbsView(View):
    f = None 
    template_name = None 
    def get(self,request,*args, **kwargs):
        account = Account.objects.first().balance()
        
        form = self.f()
        context = {
            'form':form,
        }
        return render(request , self.template_name ,context)
    
    def post(self,request,*args,**kwargs):
        form = self.f(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            self.save_model(obj)
        else:
            print(form.errors)
        context = {
        'form':form,
        }
        return render(request , self.template_name,context)
    
    def save_model(self,obj):
        obj.save()

# class AccountTypeView(AbsView):
#     f = AccountTypeForm 
#     template_name = 'account_page.html'

class CurrencyView(AbsView):
    f = CurrencyForm 
    template_name = 'account_page.html'
  
def view2(request):
    # raise Exception('error')
    return JsonResponse({'status':1,'data':'response ok'})

def view3(request,id,name):
    return HttpResponse('view3')

class AccountTypeView(View): 
    def get(self, request, *args, **kwargs):
        account_types = AccountType.objects.all()
        if 'id' in request.GET.keys():
            account_type = AccountType.objects.get(id=request.GET.get('id'))
            form = AccountTypeForm(instance=account_type)
        else:
            form = AccountTypeForm()
        context = {
            'form': form,
            'data': account_types,
            'url' : reverse('account_type'),
            'id' : request.GET.get('id')
        }
        return render(request, 'account_type.html', context)
    
    def post(self, request, *args, **kwargs):
        account_types = AccountType.objects.all()
        if 'id' in request.POST.keys():
            account_type = AccountType.objects.get(id=request.POST.get('id'))
            form = AccountTypeForm(request.POST, instance=account_type)
            
        else :
            form = AccountTypeForm(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(type(form),'form_type')
            obj = form.save()
            print(type(obj),'form_type2')
            # form.save()
        context = {
            'form': form,
            'data':account_types,
            'url' : reverse('account_type')
            # 'cleaned_data':cleaned_data
        }
        return render(request, 'account_type.html', context)
    

from django_datatables_view.base_datatable_view import BaseDatatableView
class AccountTypeJson(BaseDatatableView):
    model = AccountType
    columns = [
        'id',
        'name',
        'description'
    ]