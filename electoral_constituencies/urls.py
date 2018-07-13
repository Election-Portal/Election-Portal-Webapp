from django.urls import path
from electoral_constituencies.views import show_all_sabhas, show_filter_sabhas, pratinidhi_sabha_details, pradesh_sabha_details
from political_divisions.views import show_district_options

urlpatterns = [
    path('', show_all_sabhas, name="AllConstituences"),
    path('show-district-options/', show_district_options, name="ShowDistrictOptions"),
    path('<str:province>/<str:district>/', show_filter_sabhas, name="ShowFilterSabhas"),
    path('pratinidhi-sabha-<int:pratinidhi_sabha_pk>-details/', pratinidhi_sabha_details, name="PratinidhiSabhaDetails"),
    path('pradesh-sabha-<int:pradesh_sabha_pk>-details/', pradesh_sabha_details, name="PradeshSabhaDetails"),

]