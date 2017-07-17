
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
# from .forms import UserForm
from .models import Student, Admin, RsoGroup, Event
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from rso.forms import SignUpForm


def index(request):
    allRSOs = RsoGroup.objects.all()

    context = {
        'allRSOs': allRSOs
    }
    return render(request, 'rso/index.html', context)


def detail(request, uID):
    user = get_object_or_404(User, pk=uID)

    context = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
    return render(request, 'rso/detail.html', context)


def map(request):

    return render(request, 'rso/map.html')


def profile(request):

    events = []

    for event in Event.objects.all():
        events.append(event)

    context = {
        'events': events,
    }

    return render(request, 'rso/profile.html', context=context)


def registration(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)

        user = user.save()

        student = Student.objects.create_student(user=user)
        student.save()

        return render(request, 'rso/index.html')

    if request.method == 'GET':
        return render(request, 'rso/registration_form.html')


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            student = Student.objects.create_student(user=user)
            student.save()

            return redirect('rso:index')
    else:
        form = SignUpForm()
    return render(request, 'rso/signup.html', {'form': form})

