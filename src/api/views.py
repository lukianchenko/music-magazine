from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import ArticleSerializer, CustomerSerializer
from magazine.models import Article


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_object(self):
        return Article.objects.get(uuid=self.kwargs.get("uuid"))
