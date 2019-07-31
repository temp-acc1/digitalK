# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=80)	#name of student
	group=models.CharField(max_length=3)	#otryad
	vallet=models.IntegerField()			#amount of kuhmarka


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	subject=models.CharField(max_length=40)