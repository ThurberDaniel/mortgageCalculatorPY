from django.shortcuts import render
from django.http import HttpResponse
import math


def home(request):
    return render(request, 'calculator/home.html')


def calculating(request):
#   const r = (interest * 0.01) / 12;
#   const n = term * 12;
#   const p = amount;

    interest = float(request.GET.get('interest'))
    amount = float(request.GET.get('amount'))
    term = float(request.GET.get('term'))

    r = (interest * 0.01)/12
    n = term * 12 
    p = amount

#   const balance = ((r * p * n) / (1 - Math.pow(1 + r, -n))).toFixed(2);
#   const pmt = (balance / n).toFixed(2);
    balance = ((r * p * n) / (1 - math.pow(1+ r, - n)))
    pmt = (balance / n)
#       // console.log({ amount, interest, term });
#   // console.log({ balance, pmt });
    print(r,n,p)
    print('****')
    print(balance,pmt)
    return render(request, 'calculator/home.html',{'bal': balance , 'payment': pmt})
