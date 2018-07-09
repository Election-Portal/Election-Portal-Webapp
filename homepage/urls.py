from django.urls import path
from homepage.views import show_homepage

urlpatterns = [
    path('', show_homepage, name="HomePage"),
]