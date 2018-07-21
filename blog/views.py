from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from blog.models import Article, Category
from blog.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ArticlesList', args=[]))
    else:
        form = ArticleForm()

    template_name = 'blog/new_article.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)

@login_required
def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ArticleDetail', kwargs={'pk':pk,}))
    else:
        form = ArticleForm(instance = article)

    template_name = 'blog/update_article.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)




def article_list(request):
    articles = Article.objects.all().order_by('-published_on')
    popular_articles = articles.filter(is_popular=True)[:5]
    more_on_articles = articles.filter(is_more_on=True)[:5]
    most_active_articles = articles.filter(is_most_active=True)[:5]
    print(popular_articles)
    template_name = 'blog/list.html'
    context = {
        "articles": articles,
        "more_on_articles":more_on_articles,
        "popular_articles":popular_articles,
        "most_active_articles":most_active_articles,

    }
    return render(request, template_name, context)

def article_detail(request, pk):
    articles = Article.objects.all().order_by('-published_on')
    latest_three_articles = articles[:3]
    article = get_object_or_404(Article, pk=pk)
    template_name = 'blog/detail.html'
    context = {
        'article': article,
        'latest_three_articles': latest_three_articles,
        'articles': articles
    }
    return render(request, template_name, context)