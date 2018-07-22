from django.db import models

# Create your models here.

class About (models.Model):
    about = models.TextField(default="This porject is for providing the basc of Election results and more. ...")
    get_involved = models.TextField(default="This project is opensource and you can contribure and get involved when ever you like ...")
    faq = models.TextField(default="Some of the FAQ will be answered here, if you are looking for FQA about getting involved please check the get involved page. ...")
    contact = models.TextField(default="You can contact us through emails, github or more ...")
