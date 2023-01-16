from django.urls import include, path
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from api.views import UserViewSet, CreateArticleView, ArticleDetailView, UpdateArticleView, DeleteArticleView, ArticleListView

app_name = "api"

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

schema_view = get_schema_view(openapi.Info(
        title="Ukrainian music magazine API",
        default_version='v1',
        description="Music magazine API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path("auth/", include('djoser.urls.jwt')),
    path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name='swagger_docs'),
    path("articles/", CreateArticleView.as_view(), name="create_article", ),
    path("articles/", ArticleListView.as_view(), name="articles_list"),
    path("articles/<uuid:uuid>/retrieve/", ArticleDetailView.as_view(), name="article_details"),
    path("articles/<uuid:uuid>/update/", UpdateArticleView.as_view(), name="update_article"),
    path("articles/<uuid:uuid>/delete/", DeleteArticleView.as_view(), name="delete_article"),
]
