from blog.models import Category, Article
from django.forms import ModelForm

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ('author',)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
    