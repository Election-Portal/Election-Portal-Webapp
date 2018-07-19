from django.db import models

# Create your models here.


class PoliticalParty(models.Model):
    name = models.CharField("Name of Party", max_length=50)
    party_logo = models.ImageField(upload_to="party_logo")
    founded_on = models.DateField("Date of Establishment", auto_now=False, auto_now_add=False)
    ideology = models.TextField()
    seats_in_pradessabha = models.IntegerField()
    seats_in_pratinidhisabha = models.IntegerField()
    chief_of_party = models.CharField("President of Party", max_length=50)
    about = models.TextField()
    headquarter = models.CharField("Headquarter Location", max_length=50)

    class Meta:
        verbose_name = "Political Party"
        verbose_name_plural = "Political Parties"

    def __str__(self):
        return self.name
