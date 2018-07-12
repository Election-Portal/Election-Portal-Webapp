from django import forms
from django.forms import ModelForm
from political_parties.models import PoliticalParty

class PoliticalPartyForm(forms.ModelForm):
    """Form definition for PoliticalParty."""

    class Meta:
        """Meta definition for PoliticalPartyform."""

        model = PoliticalParty
        fields = '__all__'
