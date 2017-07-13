# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse

import datetime

#

# queries  can be done with'objects'
# someModel.bojects.all()  yields all objects
# someModel.bojects.filter( somefield='valueOfField' )  yields objects with column: someField and value: value of field
# someModel.bojects.exclude( somefield='valueOfField' ) exclude objects with column: someField and value: value of field



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    member = models.ManyToManyField('RsoGroup', blank=True)

    aboutMe = models.TextField()

    def get_absolute_url(self):
        return reverse('rso:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.user.username)


class Admin(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class RsoGroup(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    numStudents = models.IntegerField(verbose_name='Number of Student')

    address = models.CharField(max_length=250)
    lon = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    address = models.CharField(max_length=250)
    lon = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)

    PUBLIC = 'pub'
    PRIVATE = 'pri'
    RSO = 'rso'
    visChoices = (
        (PUBLIC, 'Public Event'),
        (PRIVATE, 'Private Event'),
        (RSO, 'RSO Event'),
    )

    visibility = models.CharField(max_length=3, choices=visChoices, default=PUBLIC)

    GENERAL = 'gen'
    FUNDRAISING = 'fun'
    SOCIAL = 'soc'
    TECH = 'tec'

    catChoices = (
        (GENERAL, 'General'),
        (FUNDRAISING, 'Fund Raising'),
        (SOCIAL, 'Social'),
        (TECH, 'Tech Talk'),
    )

    category = models.CharField(max_length=3, choices=catChoices, default=GENERAL)

    rso = models.ForeignKey(RsoGroup, on_delete=models.CASCADE, blank=True, null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
