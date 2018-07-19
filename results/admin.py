from django.contrib import admin
from results.models import PradeshSabhaResult, PratinidhiSabhaResult, Result
from candidates.models import Nominee
# Register your models here.


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    '''Admin View for Result'''



# @admin.register(PratinidhiSabhaResult)
# class PratinidhiSabhaResultAdmin(admin.ModelAdmin):
#     '''Admin View for PratinidhiSabhaResult'''

#     list_display = ('year', 'pratinidhisabha', 'is_declared')

# @admin.register(PradeshSabhaResult)
# class PradeshSabhaAdmin(admin.ModelAdmin):
#     '''Admin View for PradeshSabhaResult'''

#     list_display = ('year', 'pradeshsabha', 'is_declared')
