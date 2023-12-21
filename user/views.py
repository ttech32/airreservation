from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .decorators import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import *
from dashboard.models import *

# Create your views here.
def Home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'home.html')
    return render(request, 'home.html')

@login_required(login_url='home')
@Authenticated
@Role
def Index(request):
    flight = request.user.users.flight
    context = {'flight':flight}
    return render(request, 'index.html', context)

@login_required(login_url='home')
@Authenticated
@Role
def user_profile(request):
    
    context = {}
    return render(request, 'user_profile.html', context)

def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Blog(request):
    return render(request, 'blog.html')


def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            #phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
        
            user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password,
                
                
            )
            
            Passenger.objects.create(
                user = user,
            )
            #user.profile.phone_number = phone_number
            #user.profile.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegistrationForm()
            
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='home')
def Logout_view(request):
    logout(request)
    return render(request, 'home.html')

