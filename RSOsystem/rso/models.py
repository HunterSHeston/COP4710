# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from geoposition.fields import GeopositionField



class StudentManager(models.Manager):
    def create_student(self, user):
        student = self.create(user=user)

        return student


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    university = models.ForeignKey('University', on_delete=models.CASCADE, blank=True, null=True)
    member = models.ManyToManyField('RsoGroup', blank=True)
    aboutMe = models.TextField()

    objects = StudentManager()

    def get_absolute_url(self):
        return reverse('rso:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.user.username)



class RsoGroup(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    students = models.ManyToManyField(Student, related_name='rsoToStudent')

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    numStudents = models.IntegerField(verbose_name='Number of Student')

    def __str__(self):
        return self.name


class Event(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    time = models.DateTimeField( blank=True, null=True)

    location = GeopositionField(null=True, blank=True)

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

    rso = models.ForeignKey(RsoGroup, on_delete=models.CASCADE, blank=True, null=True, related_name='rso')
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university')

    def __str__(self):
        return self.name
