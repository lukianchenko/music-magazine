from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import ArticleSerializer, CustomerSerializer
from magazine.models import Article


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CreateArticleView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_object(self):
        return Article.objects.get(uuid=self.kwargs.get("uuid"))


class UpdateArticleView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_object(self):
        return Article.objects.get(uuid=self.kwargs.get("uuid"))


class DeleteArticleView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_object(self):
        return Article.objects.get(uuid=self.kwargs.get("uuid"))

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
