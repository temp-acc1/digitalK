# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

GROUP_CHOICES = (
	('B1', 'B1'),
	('B1', 'B2'),
	('B1', 'C1'),
	('B1', 'C2'),
	)


# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=80)
	group=models.CharField(max_length=3, choices=GROUP_CHOICES)
	wallet=models.IntegerField()
	age=models.IntegerField()


class Teacher(models.Model):
	name=models.CharField(max_length=80)
	subject=models.CharField(max_length=80)