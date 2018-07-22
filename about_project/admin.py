from django.contrib import admin

from about_project.models import About
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    '''Admin View for About Project'''
