from django.shortcuts import render
from django.http import HttpResponse
from features.models import Bio
# Create your views here.
def fun(request):
    return render(request,'home.html')


def res(request):
    key=Bio.objects.all()
    return render(request,'result.html',{'data':key})

def res1(request):
    key=Bio.objects.all()
    return render(request,'customer.html',{'data':key})

def customer1(request):
    key=Bio.objects.get(id=5)
    result={
    'customer_no':key.customer_no,
    'Name':key.Name,
    'Email':key.Email,
    'Amount':key.Amount
    }
    return render(request,'customer1.html',result)

def customer2(request):
    key=Bio.objects.get(id=6)
    result={
    'customer_no':key.customer_no,
    'Name':key.Name,
    'Email':key.Email,
    'Amount':key.Amount
    }
    return render(request,'customer1.html',result)

def customer3(request):
    key=Bio.objects.get(id=7)
    result={
    'customer_no':key.customer_no,
    'Name':key.Name,
    'Email':key.Email,
    'Amount':key.Amount
    }
    return render(request,'customer1.html',result)

def customer4(request):
    key=Bio.objects.get(id=8)
    result={
    'customer_no':key.customer_no,
    'Name':key.Name,
    'Email':key.Email,
    'Amount':key.Amount
    }
    return render(request,'customer1.html',result)

def customer5(request):
    key=Bio.objects.get(id=9)
    result={
    'customer_no':key.customer_no,
    'Name':key.Name,
    'Email':key.Email,
    'Amount':key.Amount
    }
    return render(request,'customer1.html',result)

def transaction(request):
    return render(request,'transaction.html')

def receiver(request):
    if request.method == 'POST':
        value=int(request.POST.get('tamount'))
        a=int(request.POST.get('cnumber'))
        b=int(request.POST.get('unumber'))
        num=a+4
        key=Bio.objects.get(id=num)
        key.Amount+=value
        key.save()
        num1=b+4
        key=Bio.objects.get(id=num1)
        key.Amount-=value
        key.save()
        total_amount=key.Amount
        return render(request,'receiver.html')
      