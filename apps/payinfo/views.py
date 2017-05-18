#encoding: utf-8
from django.shortcuts import render

def payinfo_list(request):
    return render(request,'payinfo/payinfo.html')
