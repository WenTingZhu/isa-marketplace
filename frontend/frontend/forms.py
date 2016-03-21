from django import forms
# from .phone_field import PhoneField
# from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField

# todo: required keyword is not doing anything

class SignupForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput, required=True)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(label='First Name',max_length=100, widget=forms.TextInput, required=True)
    last_name = forms.CharField(label='Last Name',max_length=100, widget=forms.TextInput, required=True)
    # todo: phonefield
    phone = forms.CharField(label='Phone Number', widget=forms.TextInput)
    school = forms.CharField(label='School Name',max_length=100, widget=forms.TextInput, required=True)




    # email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'], phone=data['phone'], school=['school'], rating=0


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput, required=True)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput, required=True)
