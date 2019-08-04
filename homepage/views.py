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
	try:
		a = request.user.Student.wallet
	except:
		return render(request,'home.html',{'request':request,'class':True})
	else:
		return render(request,'home.html',{'request':request,'class':False})


def login_page(request):
	if request.method == 'POST':
		usname = request.POST['username']
		pasword = request.POST['password']
		us = authenticate(request,username=usname, password=pasword)
		if us is not None:
			login(request,us)
			return redirect('/')
		else:
			return render(request,'login.html',{'errors':"There's no such user. Try again!",'request':request})
	return render(request, 'login.html',{'errors':''})


def logout_page(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/login')
	else:
		return HttpResponse(404)


def accpage(request):
	if request.method=='GET':
		try:
			a = request.user.student.wallet
		except:
			return render(request,'cabinet.html',{'request':request,'class':True})
		else:
			return render(request,'cabinet.html',{'request':request,'class':False})
	else:
		if request.POST.get('transfer'):
			return HttpResponse('t')
		elif request.POST.get('top_up'):
			return HttpResponse('u')

def transfer(request):
	return HttpResponse('t')



def topup(request):
	return HttpResponse('U')

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
