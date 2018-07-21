from django.shortcuts import render, get_object_or_404
from results.models import Result
from political_divisions.models import Province, District
from electoral_constituencies.models import PradeshSabha, PratinidhiSabha
from candidates.models import Nominee
# Create your views here.


def show_all_results(request):
    all_results = Result.objects.all()
    all_province = Province.objects.all()
    all_district = District.objects.all()
    template_name = "results/list.html"
    context = {
        "all_results":all_results,
        "all_province":all_province,
        "all_district":all_district,
    }
    return render(request, template_name, context)

def show_filter_sabhas(request, province, district):
    all_pradesh_sabhas = PradeshSabha.objects.all()
    all_pratinidhi_sabhas = PratinidhiSabha.objects.all()
    all_province = Province.objects.all()
    all_district = District.objects.all()

    filter_pradesh_sabhas = PradeshSabha.objects.filter(province__name=province, district__id=district)
    filter_pratinidhi_sabhas = PratinidhiSabha.objects.filter(province__name=province, district__id=district)

    template_name = "results/filter_list.html"
    context = {
        "filter_pradesh_sabhas":filter_pradesh_sabhas,
        "filter_pratinidhi_sabhas":filter_pratinidhi_sabhas,
        "all_pradesh_sabhas":all_pradesh_sabhas,
        "all_pratinidhi_sabhas":all_pratinidhi_sabhas,
        "all_province":all_province,
        "all_district":all_district,

    }
    return render(request, template_name, context)


def pratinidhisabha_result_details(request,pratinidhi_sabha_pk):
    pratinidhisabha = get_object_or_404(PradeshSabha,pk=pratinidhi_sabha_pk)
    contesting_candidates = Nominee.objects.filter(object_id=pratinidhisabha.id)
    # test = Nominee.objects.get(id=1)
    # # print(test.NomineeSabhaSet.all())
    # print(test.content_object)
    # print(pratinidhisabha)
    # print(contesting_candidates)
    # print("________________________________________________________--")
    template_name = "results/pratinidhisabha_result_details.html"
    context = {
        "pratinidhisabha":pratinidhisabha,
        "contesting_candidates":contesting_candidates,
    }
    return render(request, template_name, context)

def pradeshsabha_result_details(request,pradeshsabha_pk):
    pradeshsabha = get_object_or_404(PradeshSabha,pk=pradeshsabha_pk)
    contesting_candidates = Nominee.objects.filter(object_id=pradeshsabha.id)

    template_name = "results/pradeshsabha_result_details.html"
    context = {
        "pradeshsabha":pradeshsabha,
        "contesting_candidates":contesting_candidates,
    }
    return render(request, template_name, context)