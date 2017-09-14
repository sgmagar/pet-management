from django import forms

from django.contrib.auth.models import User

from pet.models import Cat, Dog


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username', 'required':'required'}))
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'required':'required'}))


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Birthday'}),
        }


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Birthday'}),
        }

