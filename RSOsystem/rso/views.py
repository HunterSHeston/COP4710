
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student, RsoGroup, Event
from django.contrib.auth.models import User, Group
from rso.forms import SignUpForm
from django.contrib.auth.decorators import login_required


def index(request):
    allRSOs = RsoGroup.objects.all()

    context = {
        'allRSOs': allRSOs
    }
    return render(request, 'rso/index.html', context)


def map(request):

    events = Event.objects.filter(visibility=Event.PUBLIC)

    context = {
        'events': events,
    }

    return render(request, 'rso/map.html', context=context)


@login_required(login_url='/login/')
def profile(request):

    publicEvents = Event.objects.filter(visibility=Event.PUBLIC)
    rsoEvents = Event.objects.all()
    studentRsos = request.user.student.rsoToStudent.all()

    RSOs = RsoGroup.objects.filter(students=request.user.student)

    events = []

    for event in publicEvents:
        events.append(event)

    for event in rsoEvents:
        if event.rso in studentRsos and event not in events :
            events.append(event)

    context = {
        'events': events,
        'RSOs': RSOs,
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


@login_required(login_url='/login/')
def joinRso(request):

    rsos = RsoGroup.objects.all()
    return render(request, 'rso/joinRso.html', {'rsos': rsos})


@login_required(login_url='/login/')
def add(request, rsoID):

    rso = RsoGroup.objects.get(id=rsoID)
    rso.students.add(request.user.student)
    rso.save()

    rsos = RsoGroup.objects.all()
    return render(request, 'rso/joinRso.html', {'rsos': rsos})


@login_required(login_url='/login/')
def createRso(request):

    if request.method == 'POST':
        newRso = RsoGroup(
            name=request.POST['RSO_name'],
            description=request.POST['RSO_description'],
            phone=request.POST['RSO_phone'],
            email=request.POST['RSO_email']
        )

        allRSOs = RsoGroup.objects.all()

        context = {
            'allRSOs': allRSOs
        }

        creator = User.objects.get(username=request.user.username)
        creator.is_staff = True

        admins = Group.objects.get(name='Admin')
        creator.groups.add(admins)

        newRso.save()
        newRso.students.add(creator.student)
        newRso.save()


        creator.save()

        return render(request, 'rso/index.html', context=context    )

    return render(request, 'rso/createRso.html')
