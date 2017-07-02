# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return HttpResponse('Logged in with name %s' % request.user.username)


def detail(request, group_id):
    return HttpResponse("You're looking at group %s" %  group_id)

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
