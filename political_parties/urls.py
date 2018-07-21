from django.urls import path
from political_parties.views import political_parties_list, political_parties_detail, add_political_party, update_political_party

urlpatterns = [
    path('', political_parties_list, name="AllPoliticalParties"),
    path('details-<int:pk>', political_parties_detail, name="PoliticalPartyDetail"),
    path('add-political-party/', add_political_party, name="AddPoliticalParty"),
    path('update-political-party/<int:pk>/', update_political_party, name="UpdatePoliticalParty"),

]