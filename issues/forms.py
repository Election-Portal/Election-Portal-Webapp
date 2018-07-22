from django import forms
from django.forms import ModelForm
from issues.models import Complain

class ComplainForm(forms.ModelForm):
    """Form definition for Complain."""

    class Meta:
        """Meta definition for Complainform."""

        model = Complain
        exclude = ('url',)
        widgets = {
        'url': forms.TextInput(attrs={'disabled': True}),
    }
