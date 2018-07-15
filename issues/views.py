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

# class HomepageView(View):
#     form_class = ComplainForm
#     template_name = 'homepage/index.html'

#     def post(self, request, *args, **kwargs):
#         complain_form = self.form_class(request.POST, request.FILES, request)
#         if complain_form.is_valid():
#             complain_form.save()
#             return HttpResponseRedirect(reverse('HomePage'))
#         context = {
#             'complain_form':complain_form,
#         }
#         return render(request,self.template_name, context)
    
#     def get(self, request, *args, **kwargs):
#         current_url = self.request.build_absolute_uri
#         complain_form = self.form_class(initial={'url':current_url})
#         context = {
#             'complain_form':complain_form,
#         }
#         return render(request,self.template_name,context)

