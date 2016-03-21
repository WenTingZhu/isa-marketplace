from django import forms


class SignupForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}), required=True)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '*********'}), required=True)
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'John'}), required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Doe'}), required=True)
    # todo: phonefield
    phone = forms.CharField(label='Phone Number', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '777-777-7777'}))
    school = forms.CharField(label='School Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'University of Virginia'}), required=True)


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}), required=True)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '*******'}), required=True)


class HTMLDateTimeInput(forms.DateInput):
    input_type = 'datetime-local'


class CreateRideForm(forms.Form):
    open_seats = forms.IntegerField(label="Open Seats", min_value=1, max_value=10, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '1', 'style': 'width: 250px; float: right;'}))
    departure = forms.DateTimeField(label="Departure", input_formats=['%Y-%m-%dT%H:%M'], widget=HTMLDateTimeInput(
        attrs={'class': 'form-control', 'style': 'width: 250px; float: right;'}))
