from django.urls import path
# from political_divisions.views import add_province
from political_divisions.views import ProvinceFormView, show_district_options
urlpatterns = [
    # path('add-new-province/', add_province, name = "Add Province"),
    path('add-new-province/',ProvinceFormView.as_view(),name="Add Province"),
    path('show-district-options/', show_district_options, name="ShowDistrictOptions"),

]