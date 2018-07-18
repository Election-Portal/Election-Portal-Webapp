from django.urls import path
from blog.views import article_list, article_detail, add_article, update_article
urlpatterns = [
    path('', article_list, name="ArticlesList"),
    path('<int:pk>/', article_detail, name="ArticleDetail"),
    path('new-article/', add_article, name="AddArticle"),
    path('update-article/<int:pk>/', update_article, name="UpdateArticle"),
]