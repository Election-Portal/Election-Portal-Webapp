from django.shortcuts import render, HttpResponse
from issues.forms import ComplainForm

# Create your views here.

# class ComplainFormView(View):
#     form_class = ComplainForm
#     initial = {'url':'https://ww.face.com'}
#     template_name = 'homepage/index.html'

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Complain Saved Successfully.")
#         context = {
#             'complain_form':complain_form,
#         }
#         return render(request,self.template_name, context)
    
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         context = {
#             'form':form,
#         }
#         return render(request,self.template_name,context)
