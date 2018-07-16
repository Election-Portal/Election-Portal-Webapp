from django import template
from issues.forms import ComplainForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
register = template.Library()


@register.inclusion_tag('include/feedback.html')
def show_complain_form(request):
    if request.method == "POST":
            complain_form = ComplainForm(request.POST, request.FILES)

            if complain_form.is_valid():
                complain_form.save()
                return HttpResponseRedirect(reverse('HomePage'))
    else:
        complain_form = ComplainForm()
    return {'complain_form':complain_form}