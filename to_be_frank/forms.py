from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password')
        if password != password2:
            raise forms.ValidationError("Password must match")
        return password2

    def clean_email(self):
        data = self.cleaned_data.get('password')
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email is already used")
        return data

    def clean_username(self):
        data = self.cleaned_data.get('username')
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("This username is already used")
        return data
