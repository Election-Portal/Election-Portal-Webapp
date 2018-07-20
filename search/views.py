from django.shortcuts import render
from django.db.models import Q
from candidates.models import Nominee
from electoral_constituencies.models import PratinidhiSabha, PradeshSabha
from political_parties.models import PoliticalParty
from political_divisions.models import Province, District


# Create your views here.

def search_result(request):
    # all_candidates = Nominee.objects.all()
    # all_pratinidhi_sabha = PratinidhiSabha.objects.all()
    # all_pradesh_sabha = PradeshSabha.objects.all()
    # all_political_parties = PoliticalParty.objects.all()
    # all_provinces = Province.objects.all()
    # all_districts = District.objects.all()

    query_string = request.GET.get('search_q')
    if query_string:
            all_candidates = Nominee.objects.filter(
                Q(full_name__icontains=query_string)
            ).distinct()

            all_pratinidhi_sabha = PratinidhiSabha.objects.filter(
                Q(name__icontains=query_string)
            ).distinct()

            all_pradesh_sabha = PradeshSabha.objects.filter(
                Q(name__icontains=query_string)
            ).distinct()

            all_provinces = Province.objects.filter(
                Q(name__icontains=query_string)
            ).distinct()
            all_political_parties = PoliticalParty.objects.filter(
                Q(name__icontains=query_string)
            ).distinct()

    template_name = "search/result_list.html"
    context = {
        "all_candidates":all_candidates,
        "all_pratinidhi_sabha": all_pratinidhi_sabha,
        "all_pradesh_sabha": all_pradesh_sabha,
        "all_political_parties": all_political_parties,
        "all_provinces":all_provinces,
        "query_string":query_string,
    }

    return render(request, template_name, context)
