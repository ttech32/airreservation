from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from dashboard.models import *

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    #phone_number = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username has already been taken!!!")
        return username
    
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('passwords to not match')
        return confirm_password
        
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'inn', 'placeholder':'Full Name'}),
            'email':forms.TextInput(attrs={'class': 'inn', 'placeholder':'Email'}),
            'phone_number':forms.TextInput(attrs={'class': 'inn', 'placeholder':'Phone No'}),
            'address':forms.TextInput(attrs={'class': 'inn', 'placeholder':'Address'}),
            'next_of_kin':forms.TextInput(attrs={'class': 'inn', 'placeholder':'Next of Kin'}),
            'next_of_kin_number':forms.TextInput(attrs={'class': 'inn', 'placeholder':'Next of Kin Number'}),
            'flight': forms.Select(attrs={'class': 'opt'})
        }   
    '''full_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=150)
    address = forms.CharField(max_length=150)
    next_of_kin = forms.CharField(max_length=150)
    next_of_kin_number = forms.CharField(max_length=150)
    flight = forms.CharField(widget=forms.Select)'''
    
           
    