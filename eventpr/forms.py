from django import forms
from .models import Registration

# Creation of forms
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

        labels={
            'cus_name':'Customer Name',
            'cus_contact':'Customer Contact',
            'name':'Event Name',
            'registered_on':'Registration Date',
            }