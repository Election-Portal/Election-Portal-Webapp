from django.urls import path
from volunteers.views import VolunteerSignUpView

urlpatterns = [
    path('signup/', VolunteerSignUpView.as_view(), name="VolunteerSignUp"),
]