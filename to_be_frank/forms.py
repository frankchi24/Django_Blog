from django import forms


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
