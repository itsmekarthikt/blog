from django import forms
from django.contrib.auth.models import User  
from .models import contactus
from django.contrib.auth import authenticate


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Name',required=True)
    email = forms.EmailField(label='Email',required=True)
    message = forms.CharField( label='Message',required=True)

    class Meta:
        model = contactus
        fields = ['name', 'email', 'message',]


class RegistrationForm(forms.ModelForm):
    username= forms.CharField(max_length=150, label='Username', required=True)
    email = forms.EmailField(label='Email', max_length=100,required=True)
    password = forms.CharField( label='Password', max_length=100, required=True)
    confirm_password = forms.CharField( label='Confirm_Password',max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password do not match"
            )
        

class LoginForm(forms.Form):
    username=forms.CharField( label='Username', required=True)
    password=forms.CharField( label='Password',  required=True)


    def clean(self):
        cleaned_data = super().clean()
        cleaned_password = cleaned_data.get("password")
        cleaned_username = cleaned_data.get("username")

        

        if cleaned_username and cleaned_password:
            user = authenticate(username=cleaned_username, password=cleaned_password)
            if user is None:
                raise forms.ValidationError(
                    "Invalid username or password"
                )



class Forgot_passwordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100,required=True)

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email address.")
        return email
    

class Reset_passwordForm(forms.Form):
    new_password = forms.CharField( label='New_Password', max_length=100, required=True)
    confirm_password = forms.CharField( label='Confirm_Password',max_length=100, required=True)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError(
                "New Password and Confirm Password do not match"
            )