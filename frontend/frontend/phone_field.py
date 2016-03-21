from django.core.validators import RegexValidator
from django import forms


class PhoneField(forms.MultiValueField):

    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                error_messages={'incomplete': 'Enter a country calling code.'},
                 validators=[RegexValidator(
                     r'^[0-9]+$', 'Enter a valid country calling code.')]),
            forms.CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                      validators=[RegexValidator(
                          r'^[0-9]+$', 'Enter a valid phone number.')]),
            forms.CharField(
                validators=[
                    RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
                      required=False),
        )
        super(PhoneField, self).__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, *args, **kwargs)
