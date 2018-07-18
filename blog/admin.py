from django.contrib import admin
from blog.models import Article, Category
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    '''Admin View for Article'''

    list_display = ('title', 'author', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('title',)