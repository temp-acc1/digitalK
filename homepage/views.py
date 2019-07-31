# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from homepage.models import Student, Teacher

# Create your views here.
def home(request):
	return render(request,'home.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		return HttpResponse(username)
	form = AuthenticationForm()
	return render(request, 'login.html',{"form":form})