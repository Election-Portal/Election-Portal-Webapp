from django.contrib import admin
from issues.models import Complain
# Register your models here.

@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    '''Admin View for Complain'''

    list_display = ('error_found', 'url',)
