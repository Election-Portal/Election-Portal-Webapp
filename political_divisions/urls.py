from django.urls import path
from political_divisions.views import add_province
urlpatterns = [
    path('add-new-province/', add_province, name = "Add Province"),
]