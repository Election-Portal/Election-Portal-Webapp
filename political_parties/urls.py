from django.urls import path
from political_parties.views import political_parties_list, political_parties_detail

urlpatterns = [
    path('', political_parties_list, name="AllPoliticalParties"),
    path('details-<int:pk>', political_parties_detail, name="PoliticalPartyDetail"),
]