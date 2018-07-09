from django.shortcuts import render

# Create your views here.

def show_homepage(request):
    template_name = "homepage/index.html"
    context = {

    }
    return render(request, template_name, context)
