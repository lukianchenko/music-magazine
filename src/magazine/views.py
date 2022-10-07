from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView

from magazine.models import Article


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['articles_list'] = Article.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"


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
