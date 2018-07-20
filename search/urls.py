from django.urls import path
from search.views import search_result

urlpatterns = [
    path('', search_result, name="SearchResult"),
]