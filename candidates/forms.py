from django import forms
from django.forms import ModelForm
from candidates.models import Nominee

class NomineeForm(forms.ModelForm):
    """Form definition for Nominee."""

    class Meta:
        """Meta definition for Nomineeform."""

        model = Nominee
        fields = '__all__'
