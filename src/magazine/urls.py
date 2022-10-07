from django.urls import path

from magazine.views import ArticleDetailView, ContactView, AboutView, ArticlesListView

urlpatterns = [
    path("<uuid:uuid>/", ArticleDetailView.as_view(), name="article_details"),
    path("articles/", ArticlesListView.as_view(), name="article_list"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("about-us/", AboutView.as_view(), name="about"),
]
