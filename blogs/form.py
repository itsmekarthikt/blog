from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name',required=True)
    email = forms.EmailField(label='Email',required=True)
    message = forms.CharField( label='Message',required=True)


class RegistrationForm(forms.ModelForm):
    username= forms.CharField(max_length=150, label='Username', required=True)
    email = forms.EmailField(label='Email', max_length=100,required=True)
    password = forms.CharField( label='Password', max_length=100, required=True)
    confirm_password = forms.CharField( label='Confirm_Password',max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]

