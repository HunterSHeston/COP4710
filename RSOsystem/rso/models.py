# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

import datetime

#

# queries  can be done with'objects'
# someModel.bojects.all()  yields all objects
# someModel.bojects.filter( somefield='valueOfField' )  yields objects with column: someField and value: value of field
# someModel.bojects.exclude( somefield='valueOfField' ) exclude objects with column: someField and value: value of field



class Admin(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.user.username


class Student(models.Model):
    ISA = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.ISA.username


class Rso(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    # created = models.DateField('date created', auto_now_add=True)
    users = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
