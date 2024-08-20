from django.shortcuts import render
from django.http import HttpResponse
from ..models import Currency
# Create your views here.
def view(request):
    Currency.objects.create(code = 'YER',name = "Yemeni",local= True)
    cur = Currency.objects.all()
    print(cur)    
    return HttpResponse('view1')
def view2(request,id):
    return HttpResponse('view2')
def view3(request,id,name):
    return HttpResponse('view3')