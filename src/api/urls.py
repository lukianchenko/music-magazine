from django.urls import include, path
from rest_framework import routers

from api.views import ArticleDetailView, UserViewSet

app_name = "api"
 
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("auth/", include('rest_framework.urls')),
    path("articles/<uuid:uuid>/", ArticleDetailView.as_view(), name="article_details")
]