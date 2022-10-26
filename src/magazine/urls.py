from django.urls import path
from magazine.views import ArticleDetailView, ContactView, AboutView, ArticlesListView

app_name = "magazine"

urlpatterns = [
    path("<uuid:uuid>/", ArticleDetailView.as_view(), name="article_details"),
    path("", ArticlesListView.as_view(), name="article_list"),
    ]
