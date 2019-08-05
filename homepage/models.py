# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

GROUP_CHOICES = (
	('B1', 'B1'),
	('B2', 'B2'),
	('C1', 'C1'),
	('C2', 'C2'),
	)

# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	group=models.CharField(max_length=3,choices=GROUP_CHOICES)	#otryad
	wallet=models.IntegerField()			#amount of kuhmarka


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	subject=models.CharField(max_length=40)