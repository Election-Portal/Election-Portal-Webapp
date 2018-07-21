from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from candidates.forms import NomineeForm
from candidates.models import Nominee
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

# Function Based View
@login_required
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

    

@login_required
def update_nominee(request, pk):
    nominee = get_object_or_404(Nominee, pk=pk)
    if request.method == 'POST':
        form = NomineeForm(request.POST, request.FILES, instance=nominee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('NomineeDetail', kwargs={'pk':pk,}))
    else:
        form = NomineeForm(instance = nominee)

    template_name = 'candidates/add_nominee.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)

def nominees_list(request):
    all_nominees = Nominee.objects.all().order_by('full_name')
    template_name = "candidates/list.html"
    context = {
        "all_nominees":all_nominees,
    }
    return render(request, template_name, context)

def nominee_details(request, pk):
    # Change PK with slug
    nominee = get_object_or_404(Nominee,pk=pk)
    template_name = "candidates/detail.html"
    context ={
        "nominee":nominee,
    } 
    return render(request,template_name,context)
    