from django.contrib.auth import login
from django.shortcuts import redirect, HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse
from volunteers.forms import VolunteerSignUpForm
from volunteers.models import User, Volunteer


class VolunteerSignUpView(CreateView):
    model = User
    form_class = VolunteerSignUpForm
    template_name = 'registration/volunteer_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'volunteer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(reverse('HomePage'))
