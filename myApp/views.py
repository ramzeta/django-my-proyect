from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import IntegrityError
# Create your views here.


def home(request):
    return render(request,
                  'home.html',
                  context={'sepal_length': 5.1, 'sepal_width': 3.5,
                           'petal_length': 1.4, 'petal_width': 0.2,
                           'class': "Iris Setosa"})


def login(request):
    return render(
        request,
        "registration/login.html"
    )


def password_change_done(request):
    return render(
        request,
        "registration/login.html"
    )


def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home.html')
            except IntegrityError:
                return render(request, 'registration/register.html', {'form': UserCreateForm, 'error': 'Username ya tomado, agarra otro'})
        else:
            return render(request, 'registration/register.html', {'form': UserCreateForm, 'error': 'Password no hace Match'})