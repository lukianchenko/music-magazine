from unicodedata import category
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView

from magazine.models import Article, Category


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(category__visible=True)
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(category__visible=True)
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(category__visible=True)
        return context


class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = "articles_list.html"
    queryset = Article.objects.all()
    # context_object_name = "all_articles"


class ArticleDetailView(DetailView):
    template_name = "article.html"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
