from django.urls import path
# from homepage.views import HomepageView
from homepage.views import show_homepage

urlpatterns = [
    #path('', HomepageView.as_view(), name="HomePage"),
    path('', show_homepage, name='HomePage'),
]