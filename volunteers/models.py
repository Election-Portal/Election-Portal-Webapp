from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    pass

class Volunteer(models.Model):
    REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="+")
    is_volunteer = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Volunteer"
        verbose_name_plural = "Volunteers"