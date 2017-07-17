
# from django.views import generic
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Student
#
#
# class IndexView(generic.ListView):
#     template_name = 'rso/index.html'
#
#     def get_queryset(self):
#         return Student.objects.all()
#
#
# class DetailView(generic.DetailView):
#     model = Student
#     template_name = 'rso/detail.html'
#
#
# class StudentCreate(CreateView):
#     model = Student
#     fields = ['username', 'firstname', 'lastname', 'email']






def registration(request):
    str = ''














# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
# from .forms import UserForm
from .models import Student, Admin, RsoGroup


def index(request):
    allStudents = Student.objects.all()
    context = {'allStudents': allStudents}
    return render(request, 'rso/index.html', context)



def detail(request, uID):
    student = get_object_or_404(Student, pk=uID)
    context = {
            'id': student.user.id,
            'first_name': student.user.first_name,
            'last_name': student.user.last_name,
            'email': student.user.email,

        }
    return render(request, 'rso/detail.html', context)

def add_event(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        description = request.POST['description']
        location = request.POST['location']
        email = request.POST['email']
        phone = request.POST['phone']
        visibility = request.POST['visibility']
        category = request.POST['category']
        rso = request.POST['rso']
        university = request.POST['university']

        event = Event(  name=name, description=description, location=location, email=email,
                        phone=phone, visibility=visibility, category=category, rso=rso, university=university)
        event.save()

        return redirect('/events/')
    else:
        return render(request, 'rso/add_event.html')

def event_detail(request, id):
    event = Event.objects.get(id=id)

    context = {
        'event':event
    }
    return render(request, 'rso/event_detail.html', context)


def add_rso(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        description = request.POST['description']
        email = request.POST['email']
        phone = request.POST['phone']

        rso = Rso(name=name, description=description, email=email, phone=phone)
        rso.save()

        return redirect('/rso')
    else:
        return render(request, 'rso/add_rso.html')

def rso_detail(request, id):
    rso = Rso.objects.get(id=id)

    context = {
        'rso':rso
    }
    return render(request, 'rso/event_detail.html', context)

# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'rso/registration_form.html'
#
#     #display a blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             # cleaned (normalized) data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # returns User objects if credentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('rso:index')
#         return render(request, self.template_name, {'form':form})
