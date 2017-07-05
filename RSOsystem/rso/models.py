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
	email = models.EmailField(max_length=20, default='')
	phone = models.CharField(max_length=10, default='')
	def __str__(self):
		return self.name

class Event(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    email = models.EmailField(max_length=20, default='')
    phone = models.EmailField(max_length=10, default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rso_host = models.ForeignKey(Rso, default='')
    university_host = models.ForeignKey(University)
	#location field

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=20)
	decription = models.TextField()
    email = models.EmailField(max_length=20, default='')
    phone = models.CharField(max_length=10, default='')
	num_students = models.IntegerField()
	#location field

    def __str__(self):
        return self.name
