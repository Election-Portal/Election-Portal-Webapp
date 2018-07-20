from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from issues.forms import ComplainForm
from django.urls import reverse
from blog.models import Article

# Create your views here.

def show_homepage(request):
    articles = Article.objects.all().order_by('-published_on')
    popular_articles = articles.filter(is_popular=True)[:5]
    more_on_articles = articles.filter(is_more_on=True)[:5]
    most_active_articles = articles.filter(is_most_active=True)[:5]
    template_name = 'homepage/index.html'
    context = {
        "more_on_articles":more_on_articles,
        "popular_articles":popular_articles,
        "most_active_articles":most_active_articles,

    }
    return render(request, template_name, context)


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

