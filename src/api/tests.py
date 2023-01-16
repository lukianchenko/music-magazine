from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import CustomUser
from magazine.models import Article, Category


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.author = CustomUser.objects.create(email="author@author.com", password="author")
        self.quiz = Article.objects.create(
            title="test",
            text="Sample text for article",
            category=Category.objects.create(name="NewCategory"),
            author=self.author,
        )

    def test_quiz_list(self):
        user = CustomUser.objects.create(email="admin@admin.com", password="admin")
        self.client.force_authenticate(user=user)

        result = self.client.get(reverse("api:article_details", kwargs={"uuid": self.quiz.uuid}))
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_quiz_list_wrong_user(self):
        result = self.client.get(reverse("api:article_details", kwargs={"uuid": self.quiz.uuid}))
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)
