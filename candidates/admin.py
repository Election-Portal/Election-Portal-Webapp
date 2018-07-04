from django.contrib import admin
from candidates.models import Nominee
# Register your models here.


@admin.register(Nominee)
class NomineeAdmin(admin.ModelAdmin):
    '''Admin View for Nominee'''

    list_display = ('full_name', 'political_affiliation', 'dob')
    ordering = ('full_name',)