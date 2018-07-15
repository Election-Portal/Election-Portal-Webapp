from django.db import models
from electoral_constituencies.models import PratinidhiSabha, PradeshSabha
# Create your models here.

ELECTION_YEAR_CHOICES = (
    ('2074', '2074'),
)

class Result(models.Model):
    year = models.CharField(max_length=4, choices=ELECTION_YEAR_CHOICES)

    def __str__(self):
        return self.year
    
    class Meta:
        verbose_name="Result"
        verbose_name_plural="Results"

class PratinidhiSabhaResult(Result):
    pratinidhisabha = models.ForeignKey(PratinidhiSabha, on_delete=models.CASCADE)
    is_declared = models.BooleanField(default=False)

    def __str__(self):
        return "Result of {} - {}".format(self.pratinidhisabha, self.year)
    
    class Meta:
        verbose_name = "Result of Pratinidhi Sabha"
        verbose_name_plural = "Result of Pratinidhi Sabhas"
    

class PradeshSabhaResult(Result):
    pradeshsabha = models.ForeignKey(PradeshSabha, on_delete=models.CASCADE)
    is_declared = models.BooleanField(default=False)

    def __str__(self):
        return "Result of {} - {}".format(self.pradeshsabha, self.year)
    
    class Meta:
        verbose_name = "Result of Pradesh Sabha"
        verbose_name_plural = "Result of Pradesh Sabhas"

    
    
    
