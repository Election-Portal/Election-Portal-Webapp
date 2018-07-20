from django.urls import path
from results.views import show_all_results, show_filter_sabhas, pratinidhisabha_result_details





urlpatterns = [
    path('', show_all_results, name="AllResults"),
    path('<str:province>/<str:district>/', show_filter_sabhas, name="ShowFilterSabhas"),
    path('pratinidhi-sabha-result-<int:pratinidhi_sabha_pk>-details/', pratinidhisabha_result_details, name="PratinidhiSabhaResultDetails"),
]