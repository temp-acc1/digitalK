# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from homepage.models import Student, Teacher
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	return render(request,'home.html',{'logged':request.user.is_authenticated})


def login_page(request):
	if request.method == 'POST':
		usname = request.POST['username']
		pasword = request.POST['password']
		us = authenticate(request,username=usname, password=pasword)
		if us is not None:
			login(request,us)
			return redirect('/')
		else:
			return render(request,'login.html',{'errors':"There's no such user. Try again!"})
	return render(request, 'login.html',{'errors':''})