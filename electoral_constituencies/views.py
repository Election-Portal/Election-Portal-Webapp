from django.shortcuts import render, get_object_or_404
from electoral_constituencies.models import PradeshSabha, PratinidhiSabha
from political_divisions.models import Province, District
from django.contrib.auth.decorators import login_required

# Create your views here.


def show_all_sabhas(request):
    all_pradesh_sabhas = PradeshSabha.objects.all()
    all_pratinidhi_sabhas = PratinidhiSabha.objects.all()
    all_province = Province.objects.all()
    all_district = District.objects.all()
    template_name = "electoral_constituencies/list.html"
    context = {
        "all_pradesh_sabhas":all_pradesh_sabhas,
        "all_pratinidhi_sabhas":all_pratinidhi_sabhas,
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

    template_name = "electoral_constituencies/filter_list.html"
    context = {
        "filter_pradesh_sabhas":filter_pradesh_sabhas,
        "filter_pratinidhi_sabhas":filter_pratinidhi_sabhas,
        "all_pradesh_sabhas":all_pradesh_sabhas,
        "all_pratinidhi_sabhas":all_pratinidhi_sabhas,
        "all_province":all_province,
        "all_district":all_district,

    }
    return render(request, template_name, context)

def pratinidhi_sabha_details(request, pratinidhi_sabha_pk):
    # replace pk with slug
    pratinidhi_sabha = get_object_or_404(PratinidhiSabha, pk=pratinidhi_sabha_pk)
    template_name = "electoral_constituencies/pratinidhi_sabha_details.html"
    context = {
        "pratinidhi_sabha": pratinidhi_sabha,
    }
    return render(request, template_name, context)

def pradesh_sabha_details(request, pradesh_sabha_pk):
    # replace pk with slug
    pradesh_sabha = get_object_or_404(PradeshSabha, pk=pradesh_sabha_pk)
    template_name = "electoral_constituencies/pradesh_sabha_details.html"
    context = {
        "pradesh_sabha": pradesh_sabha,
    }
    return render(request, template_name, context)

