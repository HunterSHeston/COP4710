# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class Rso(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	users = models.ManyToManyField(User)
	def __str__(self):
		return self.name
