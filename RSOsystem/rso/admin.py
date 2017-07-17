# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Student, RsoGroup, Admin, Event, University
from geoposition.fields import GeopositionField

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(RsoGroup)
admin.site.register(Event)
admin.site.register(University)
