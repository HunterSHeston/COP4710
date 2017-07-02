# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

import datetime

#


class Admin(models.Model):
    aname = models.CharField(max_length=20)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.user.name


class Student(models.Model):
    ISA = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.user.name


class Rso(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    # created = models.DateField('date created', auto_now_add=True)
    users = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.name
