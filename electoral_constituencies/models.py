from django.db import models
from political_divisions.models import Province
from political_parties.models import PoliticalParty
# Create your models here.



class Sabha(models.Model):
    name = models.CharField("Name", max_length=50)
    province = models.ForeignKey(Province, related_name="sabha_province_set",on_delete=models.CASCADE)
    area = models.IntegerField()
    population = models.IntegerField()
    voters = models.IntegerField()
    is_marginal = models.BooleanField(default=False)

class PradeshSabha(Sabha):
    winner = models.CharField("Member of Provincial Assembly", max_length=50)
    won_political_party = models.ForeignKey(PoliticalParty, related_name = "pradeshsabha_won_political_party_set",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pradesh Sabha"
        verbose_name_plural = "Pradesh Sabhas"

    def __str__(self):
        return self.name

class PratinidhiSabha(Sabha):
    winner = models.CharField("Member of House of Representative", max_length=50)
    won_political_party = models.ForeignKey(PoliticalParty, related_name = "pratinidhisabha_won_political_party_set",on_delete=models.CASCADE)
    pradeshsabha_ka = models.ForeignKey(PradeshSabha, related_name="pratinidhisabha_pradeshsabha_ka",on_delete=models.CASCADE)
    pradeshsabha_kha = models.ForeignKey(PradeshSabha, related_name="pratinidhisabha_pradeshsabha_kha",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pratinidhi Sabha"
        verbose_name_plural = "Pratinidhi Sabhas"
    
    def __str__(self):
        return self.name
