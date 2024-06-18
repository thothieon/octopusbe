

import os
import sys

from django.views.generic import View
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect

from .models import dbtest, personnelinformation

def home(request):
    print('home_init')
    if request.method == 'POST':
        print('home_POST')
        # 從 POST 請求中取得資料
        id = request.POST.get('id')
        name = request.POST.get('name')
        add = request.POST.get('add')

        # 創建並儲存新的資料物件
        obj = dbtest(id=id, name=name, add=add)
        obj.save()
        
        readData = dbtest.objects.all()
        print('readData', readData)

        return render(request, 'home.html', {'readData':readData})  # 或者重新導向到另一個頁面
    else:
        print('home_GET')
        readData = dbtest.objects.all()
        print('readData', readData)
        return render(request, 'home.html', {'readData':readData})

def PersonnelInformation(request):
    print('PersonnelInformation_init')
    
    #readData = personnelinformation.objects.all()
    #readData = personnelinformation.objects.all().order_by('id').order_by('joinYear')
    #readData = personnelinformation.objects.all().order_by('id').values()

    book_list = personnelinformation.objects.all()
    paginator = Paginator(book_list, 10)  # 每页显示50条数据
    page_number = request.GET.get('page')
    readData = paginator.get_page(page_number)
    
    #print('readData', readData.query)
    return render(request, 'PersonnelInformation.html', {'readData':readData})

def PersonnelList(request):
    print('PersonnelList_init')
    readData = personnelinformation.objects.all().order_by('id','joinYear')
    print('readData', readData.query)
    return render(request, 'homepage/PersonnelList.html', {'readData':readData})

def login(request):
    print('login_init')
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index/')
    
    print('login_01')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    print('login_02')
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        print('login_03')
        return render(request, 'homepage/login.html',  ())

def index(request):
    return HttpResponse('Hello index World!')
