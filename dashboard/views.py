from django.shortcuts import render
from .models import *
from user.decorators import *
from django.contrib.auth.decorators import login_required
from user.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='home')
@Authenticated
def flight(request):
    flight = Flight.objects.all()
    context = {'flights':flight}
    return render(request, "flight.html", context)

@login_required(login_url='home')
@Authenticated
def control(request, pk):
    flight = Flight.objects.get(id=pk)
    passengers = flight.passenger.all().order_by('-id')
    context = {'flight':flight,
               'passengers':passengers,}
    return render(request, 'control.html', context)

@login_required(login_url='home')
def book(request):
    flight = Flight.objects.all()
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            
        '''if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            next_of_kin = form.cleaned_data['next_of_kin']
            next_of_kin_number = form.cleaned_data['next_of_kin_number']
            
            flight = index[flight]
        
            passenger = Passenger.objects.create(
                full_name = full_name,
                email = email,
                phone_number = phone_number,
                address = address,
                next_of_kin = next_of_kin,
                next_of_kin_number = next_of_kin_number,
                flight = flight[flight],
                
            )'''
            
        return HttpResponseRedirect(reverse('flight'))
    context = {'form':form}# 'flights':flight}
    return render(request, 'book.html', context)

@login_required(login_url='home')
def update_passenger(request, pk):
    passenger = Passenger.objects.get(id=pk)
    form = BookForm(instance=passenger)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('flight'))
    context = {'form':form}
    return render(request, 'book.html', context)

@login_required(login_url='home')
def delete_passenger(request, pk):
    passenger = Passenger.objects.get(id=pk)
    if request.method == 'POST':
        passenger.delete()
        return HttpResponseRedirect(reverse('flight'))
    context = {'passenger':passenger}
    return render(request, 'delete.html', context)