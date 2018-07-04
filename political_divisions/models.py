from django.db import models

# Create your models here.


class Province(models.Model):
    name = models.CharField("Province Name", max_length=50)
    formation_date = models.DateField("Province was formed on", auto_now=False, auto_now_add=False)
    capital_city = models.CharField("Capital City", max_length=50)
    area = models.IntegerField()
    population = models.IntegerField()
    voters = models.IntegerField()
    chief_minister = models.CharField("Chief Minister", max_length=50)
    speaker = models.CharField(max_length=50)
    governor = models.CharField(max_length=50)
    # official_logo = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    def __str__(self):
        return self.name
    

