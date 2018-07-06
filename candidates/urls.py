from django.urls import path
from candidates.views import add_nominee

urlpatterns = [
    path('add-nominee/', add_nominee, name="Add Nominee"),
]