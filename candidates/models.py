from django.db import models
from political_parties.models import PoliticalParty
from electoral_constituencies.models import PradeshSabha, PratinidhiSabha

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Nominee(models.Model):
    full_name = models.CharField("Full Name", max_length=50)
    # Further work required. candidacy_to must include option for the location rather than the model name.
    limit = models.Q(app_label = 'electoral_constituencies', model = 'pradeshsabha') | models.Q(app_label = 'electoral_constituencies', model = 'pratinidhisabha')
    content_type = models.ForeignKey(ContentType, limit_choices_to=limit,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    political_affiliation = models.ForeignKey(PoliticalParty, related_name = "nominee_political_affiliation_set", on_delete=models.CASCADE)
    dob = models.DateField("Date of Birth", auto_now=False, auto_now_add=False)
    academic_background = models.TextField()
    awards = models.TextField()
    net_worth = models.IntegerField()
    ideology = models.TextField()
    is_incumbent = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


