from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from magazine.models import Article, Category


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(visible=True)
        categories_ids = [x.id for x in categories if x.articles_count() > 0]
        context["categories"] = Category.objects.filter(id__in=categories_ids)
        context["articles"] = Article.objects.select_related("category")
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(visible=True)
        categories_ids = [x.id for x in categories if x.articles_count() > 0]
        context["categories"] = Category.objects.filter(id__in=categories_ids)
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(visible=True)
        categories_ids = [x.id for x in categories if x.articles_count() > 0]
        context["categories"] = Category.objects.filter(id__in=categories_ids)
        return context


class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = "articles_list.html"
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Article, uuid=self.kwargs.get("uuid"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(visible=True)
        categories_ids = [x.id for x in categories if x.articles_count() > 0]
        context["categories"] = Category.objects.filter(id__in=categories_ids)
        return context
