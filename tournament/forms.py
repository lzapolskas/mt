from django import forms

from .models import School, Individual


class CodeForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('code',)  # Allows user to enter only one field of data


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ('name', 'surname', 'email', 'languages')  # The code will be attached automatically.
