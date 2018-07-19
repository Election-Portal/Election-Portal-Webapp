from django.db import models

# Create your models here.

DEVICE_CHOICES = (
    ('SP', 'Smart Phones'),
    ('TA', 'Tablet'),
    ('LC', 'Laptop Computers'),
    ('NO', 'I do not know')
)


class Complain(models.Model):
    your_email = models.EmailField()
    device = models.CharField("Device", max_length=2, choices=DEVICE_CHOICES)
    url = models.URLField()
    error_found = models.CharField("Error you found(Be Brief)", max_length=60)
    steps_to_reproduce = models.TextField("How to reproduce the error?")
    #screenshot = models.ImageField(upload_to="issues_screenshot")


    class Meta:
        verbose_name = "Complain"
        verbose_name_plural = "Complains"
    
    def __str__(self):
        return self.error_found

