from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from volunteers.models import User, Volunteer

class VolunteerSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_volunteer = False
        user.is_superadmin = False
        user.is_verified = False
        user.save()
        volunteer = Volunteer.objects.create(user=user)
        return user
