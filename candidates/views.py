from django.shortcuts import render, HttpResponse
from candidates.forms import NomineeForm
from django.views import View

# Create your views here.

# Function Based View

def add_nominee(request):
    if request.method == "POST":
        form = NomineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Nominee is addes successfully.")
    
    else:
        form = NomineeForm()
    
    template_name = "candidates/add_nominee.html"
    context = {
        'form':form,
    }
    return render(request, template_name, context)