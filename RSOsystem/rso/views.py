# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import Student, Admin, Rso

def index(request):
    all_students = Student.objects.all()
    html = ''

    for student in all_students:
        url =  str(student.id) + '/'
        html += '<a href="' + url + '">' + student.ISA.username + '</a><br>'

    return HttpResponse(html)


def details(request, rso_id):
    return HttpResponse('<h2>user: %s </h2><br><h1>id: %s</h1>' % (request.user.username, str(rso_id)))

# def loginView(request):
#     userName = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
    
#     if user is not None:
#         login(request, user)
#         print 'logged in'
#     else:
#         print 'not a user'

# def logoutView(request):
#     logout(request)
