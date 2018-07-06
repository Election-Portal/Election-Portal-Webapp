from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from political_divisions.forms import ProvinceForm

# Create your views here.


# def add_member(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('Member List', args = []))
#     else:
#         form = MemberForm()
#     template_name = 'members/new_member.html'
#     context = {
#         'form':form
#     }
#     return render(request, template_name, context)


def add_province(request):
    
    if request.method == 'POST':
        form = ProvinceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Sucess'))
    else:
        form = ProvinceForm()
    template_name = 'political_divisions/add_province.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)
