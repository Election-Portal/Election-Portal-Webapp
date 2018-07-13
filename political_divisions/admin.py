from django.contrib import admin
from political_divisions.models import Province, District

# Register your models here.

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    '''Admin View for Province'''

    list_display = ('name', 'capital_city', 'chief_minister', 'area', 'population')
    ordering = ('name',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    '''Admin View for District'''

    list_display = ('name', 'area', 'province')

    ordering = ('name',)
