from django.contrib import admin
from electoral_constituencies.models import PradeshSabha, PratinidhiSabha
# Register your models here.


@admin.register(PradeshSabha)
class PradeshSabhaAdmin(admin.ModelAdmin):
    '''Admin View for PradeshSabha'''

    list_display = ('name', 'winner', 'won_political_party')
    ordering = ('name',)


@admin.register(PratinidhiSabha)
class PratinidhiSabhaAdmin(admin.ModelAdmin):
    '''Admin View for PratinidhiSabha'''

    list_display = ('name', 'winner', 'won_political_party')
    ordering = ('name',)