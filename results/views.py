from django.shortcuts import render
from results.models import Result
# Create your views here.


def show_all_results(request):
    all_results = Result.objects.all()

    template_name = "results/list.html"
    context = {
        "all_results":all_results,
    }
    return render(request, template_name, context)