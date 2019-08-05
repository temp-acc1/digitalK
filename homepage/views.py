# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from homepage.models import Student, Teacher
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	users = Student.objects.all()
	try:
		a = request.user.Student.wallet
	except:
		return render(request,'home.html',{'request':request,'class':True,'users':users})
	else:
		return render(request,'home.html',{'request':request,'class':False,'users':users})


def login_page(request):
	if request.method == 'POST':
		usname = request.POST['username']
		pasword = request.POST['password']
		us = authenticate(request,username=usname, password=pasword)
		if us is not None:
			login(request,us)
			return redirect('/')
		else:
			return render(request,'login.html',{'errors':"Нет такого пользователя",'request':request})
	return render(request, 'login.html',{'errors':''})


def logout_page(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/login')
	else:
		return HttpResponse(404)


def accpage(request):
	try:
		a = request.user.teacher
	except:
		a = False
	else:
		a = True
	users = Student.objects.all()
	return render(request,'cabinet.html',{
	'request':request,
	'class':a,
	'students':users
	})


def transfer(request):
	if request.method == 'POST':
		count = request.POST['count']
		touser = User.objects.get(id=request.POST['who'])
		who = Student.objects.get(user=touser)
		me = Student.objects.get(user=request.user)
		if me.wallet > int(count):
			me.wallet = me.wallet - int(count)
			who.wallet = who.wallet + int(count)
			me.save()
			who.save()
		return redirect('/cabinet')
	else:
		return HttpResponse(404)


def topup(request):
	if request.method == 'POST':
		count = request.POST['count']
		touser = User.objects.get(id=request.POST['who'])
		who = Student.objects.get(user=touser)
		who.wallet+=int(count)
		who.save()
		return redirect('/cabinet')
	else:
		return HttpResponse(404)

#else:
"""
def register(request):
	if request.method=='POST':
		email=request.POST['email']
		passcode=request.POST['password']
		usname=request.POST['username']
		first=request.POST['first']
		last=request.POST['last']
		subj=request.POST['subject']
		new_user=User.objects.create_user(usname,email,passcode)
		new_user.first_name=first
		new_user.last_name=last
		new_tescher=Teacher(user=new_user, subject=subj)
		new_tescher.save()
		new_user.save()
		return redirect('/login')
	return render(request,'register.html',{'errors':'','request':request})
"""
