from django.urls import path
from candidates.views import add_nominee, nominees_list, nominee_details, update_nominee

urlpatterns = [
    path('add-nominee/', add_nominee, name="AddNominee"),
    path('', nominees_list, name = "AllNominees"),
    path('details-<int:pk>/', nominee_details, name="NomineeDetail" ),
    path('update-nominee/<int:pk>/', update_nominee, name="UpdateNominee"),

]