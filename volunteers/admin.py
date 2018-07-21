from django.contrib import admin
from volunteers.models import Volunteer
# Register your models here.

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    '''Admin View for Volunteer'''

