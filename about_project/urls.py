from django.urls import path
from about_project.views import about, contact, faq, get_involved
urlpatterns = [
    # path('', article_list, name="ArticlesList"),
    path ('about-project', about, name="AboutProject" ),
    path ('contact-us', contact, name="ContactUs" ),
    path ('faq', faq, name="FAQ" ),
    path ('get-involved', get_involved, name="GetInvolved" )
]
