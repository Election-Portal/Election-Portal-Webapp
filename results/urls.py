from django.urls import path
from results.views import show_all_results, show_filter_sabhas, pratinidhisabha_result_details, pradeshsabha_result_details, showDistrictSabhas
from political_divisions.views import show_district_options





urlpatterns = [
    path('', show_all_results, name="AllResults"),
    path('show-district-options/', show_district_options, name="ShowDistrictOptions"),
    path('district/<int:pradesh_no>/<str:district_name>/', showDistrictSabhas, name="showDistrictSabhas"),
    path('<str:province>/<str:district>/', show_filter_sabhas, name="ShowFilterSabhas"),
    path('pratinidhi-sabha-result-<int:pratinidhi_sabha_pk>-details/', pratinidhisabha_result_details, name="PratinidhiSabhaResultDetails"),
    path('pradesh-sabha-result-<int:pradeshsabha_pk>-details/', pradeshsabha_result_details, name="PradeshSabhaResultDetails"),

]