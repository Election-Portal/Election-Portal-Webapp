from django import template
from issues.forms import ComplainForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
register = template.Library()


@register.inclusion_tag('include/feedback.html')
def show_complain_form(request):
    current_url = request.build_absolute_uri
    print(current_url)
    if request.method == "POST":
            complain_form = ComplainForm(request.POST, request.FILES)

            if complain_form.is_valid():
                complain_form = complain_form.save(commit=False)
                complain_form.url = current_url
                complain_form.save()
                return HttpResponseRedirect(reverse('HomePage'))
    else:
        complain_form = ComplainForm(initial={'url':current_url})
    return {'complain_form':complain_form}
