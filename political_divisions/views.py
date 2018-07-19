from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from political_divisions.forms import ProvinceForm
from political_divisions.models import Province, District
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



# def add_province(request):
    
#     if request.method == 'POST':
#         form = ProvinceForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Hello World, Done Sucessfully.")
#     else:
#         form = ProvinceForm()
#     template_name = 'political_divisions/add_province.html'
#     context = {
#         'form':form,
#     }
#     return render(request, template_name, context)

class ProvinceFormView(LoginRequiredMixin, View):
    form_class = ProvinceForm
    initial = {'key':'value'}
    template_name = 'political_divisions/add_province.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Hello World, Done Sucessfully.")
        context = {
            'form':form,
        }
        return render(request,self.template_name, context)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form':form,
        }
        return render(request,self.template_name,context)

def show_district_options(request): 
    '''
    This function will show all the availaible districts 
    for the given province.

    '''
    province_name = request.GET.get('Province')
    province_id = Province.objects.get(name=province_name).id
    print(province_id)
    districts = [{"data":"nothing found"}]
    if province_id:
        districts = District.objects.filter(province=province_id
                                            ).values("pk", "name")
        districts = list(districts)
    return JsonResponse(districts, safe=False)
