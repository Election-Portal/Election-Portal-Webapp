from django.contrib import admin
from political_parties.models import PoliticalParty
# Register your models here.

@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    '''Admin View for PoliticalParty'''

    list_display = ('name', 'chief_of_party', 'founded_on')
    ordering = ('name',)