from django.contrib import admin

from magazine.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
