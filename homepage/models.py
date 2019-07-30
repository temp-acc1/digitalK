# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=80)
	group=models.CharField(max_length=3)
	vallet=models.IntegerField()
	age=models.IntegerField()


class Teacher(models.Model):
	name=models.CharField(max_length=80)
	subject=models.CharField(max_length=80)