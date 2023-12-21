from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=400, null=True)
    city = models.CharField(max_length=260, null=True)
    
    def __str__(self):
        return f'{self.name}({self.city})'
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, related_name='departure')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, related_name='arrival')
    duration = models.IntegerField()
    
    def __str__(self):
        return f'{self.origin} to {self.destination}'
    
class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='users')
    full_name = models.CharField(max_length=260, null=True)
    email = models.CharField(max_length=260, null=True)
    phone_number = models.CharField(max_length=260, null=True)
    address = models.CharField(max_length=350, null=True)
    next_of_kin = models.CharField(max_length=260, null=True)
    next_of_kin_number = models.CharField(max_length=260, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True, related_name='passenger')
    
    def __str__(self):
        return f'{self.full_name}'