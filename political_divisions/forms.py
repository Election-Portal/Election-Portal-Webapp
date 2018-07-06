from django import forms
from django.forms import ModelForm
from political_divisions.models import Province

class ProvinceForm(forms.ModelForm):
    """Form definition for Province."""

    class Meta:
        """Meta definition for Provinceform."""

        model = Province
        fields = '__all__'
