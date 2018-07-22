from django.shortcuts import render
from about_project.models import About


# Create your views here.
def about(request):
    article = About.objects.all()[0]
    template_name = 'about/post.html'
    about = article.about
    title = 'About this Project'
    context = {
        'about': about,
        'title': title
    }
    return render(request, template_name, context)

def get_involved(request):
    article = About.objects.all()[0]
    template_name = 'about/post.html'
    about = article.get_involved
    title = 'Get Involved'
    context = {
        'about': about,
        'title': title
    }
    return render(request, template_name, context)

def faq(request):
    article = About.objects.all()[0]
    template_name = 'about/post.html'
    about = article.faq
    title = 'Frequently Asked Questions (FAQ)'
    context = {
        'about': about,
        'title': title
    }
    return render(request, template_name, context)

def contact(request):
    article = About.objects.all()[0]
    template_name = 'about/post.html'
    about = article.contact
    title = 'Contact Us'
    context = {
        'about': about,
        'title': title
    }
    return render(request, template_name, context)
