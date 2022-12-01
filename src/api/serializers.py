from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from magazine.models import Article


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

    def get_first_name(self):
        print(self.initial_data.get('first_name'))
        return self.initial_data.get('first_name')


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ["uuid", "title", "text", "category"]
