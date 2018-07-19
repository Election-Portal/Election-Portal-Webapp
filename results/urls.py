from django.urls import path
from results.views import show_all_results





urlpatterns = [
    path('', show_all_results, name="AllResults"),
]