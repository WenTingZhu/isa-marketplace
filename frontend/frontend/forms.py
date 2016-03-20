from django import forms

class SignupForm(forms.Form):
    email = forms.CharField(label='email', max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)
