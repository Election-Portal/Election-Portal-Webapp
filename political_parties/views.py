from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from political_parties.models import PoliticalParty
from political_parties.forms import PoliticalPartyForm
from django.urls import reverse
# Create your views here.

def add_political_party(request):
    if request.method == "POST":
        form = PoliticalPartyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('HomePage'))
    else:
        form = PoliticalPartyForm()
    
    template_name = "political_parties/add_political_party.html"
    context = {
        "form":form,
    }
    return render(request, template_name, context)
# def add_nominee(request):
#     if request.method == "POST":
#         form = NomineeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Nominee is addes successfully.")
    
#     else:
#         form = NomineeForm()
    
#     template_name = "candidates/add_nominee.html"
#     context = {
#         'form':form,
#     }
#     return render(request, template_name, context)

def political_parties_list(request):
    all_political_parties = get_list_or_404(PoliticalParty)
    template_name = "political_parties/list.html"
    context = {
        "all_political_parties": all_political_parties,
    }
    return render(request, template_name, context)

def political_parties_detail(request, pk):
    # Change PK with slug
    political_party = get_object_or_404(PoliticalParty,pk=pk)
    template_name = "political_parties/detail.html"
    context = {
        "political_party":political_party,
    }
    return render(request, template_name, context)



# def member_list(request):
#     all_member = Member.objects.all().order_by('full_name')

#     # SEARCH 
#     query_string = request.GET.get('search_q')
#     if query_string:
#         all_member = all_member.filter(
#             Q(full_name__icontains = query_string)|
#             Q(bio__icontains = query_string)
#             # Q(alt__icontains = query_string)|
            
#             ).distinct()
#     template_name = 'members/list.html'
#     context = {
#         'all_member': all_member
#     }
#     if not query_string:
#         return render(request, template_name, context)
#     else:
#         return render(request, 'members/search.html', {'all_member':all_member})