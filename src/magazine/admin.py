from django.contrib import admin
from django.contrib.auth.models import Group

from magazine.models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Group)
