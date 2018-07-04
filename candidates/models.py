from django.db import models
from political_parties.models import PoliticalParty
# Create your models here.


class Nominee(models.Model):
    full_name = models.CharField("Full Name", max_length=50)
    political_affiliation = models.ForeignKey(PoliticalParty, related_name = "nominee_political_affiliation_set", on_delete=models.CASCADE)
    dob = models.DateField("Date of Birth", auto_now=False, auto_now_add=False)
    academic_background = models.TextField()
    awards = models.TextField()
    net_worth = models.IntegerField()
    ideology = models.TextField()
    is_incumbent = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


