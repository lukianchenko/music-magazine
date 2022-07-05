from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from magazine.models import Article, Category


def sample_category(name):
    return Category.objects.create(name=name)


def sample_author(first_name, last_name):
    return get_user_model().objects.create(first_name=first_name, last_name=last_name)


def sample_article(title, category, author, **params):
    defaults = {
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut"
        "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco"
        "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in"
        "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat"
        "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }
    defaults.update(params)
    return Article.objects.create(title=title, category=category, author=author, **defaults)


class TestArticleModel(TestCase):
    def setUp(self) -> None:
        self.test_author = sample_author("John", "Travolta")
        self.test_category = sample_category("Culture")
        self.test_article = sample_article("Test article", category=self.test_category, author=self.test_author)

    def tearDown(self) -> None:
        self.test_category.delete()
        self.test_author.delete()

    def test_article_creation(self):
        self.assertTrue(isinstance(self.test_article, Article))

    def test_title_limit(self):
        with self.assertRaises(ValidationError):
            sample_article(title="i" * 1025, category=self.test_category, author=self.test_author)

    def test_publish_date(self):
        self.assertEqual(
            self.test_article.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
        )

    def test_cover_image_not_null_value(self):
        self.assertIsNotNone(self.test_article.cover_image)


class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.articles_count = 5
        self.test_author = sample_author("John", "Travolta")
        self.test_category = sample_category("Culture")
        for i in range(self.articles_count):
            self.test_article = sample_article("Test article #" + str(i + 1), self.test_category, self.test_author)

    def tearDown(self) -> None:
        self.test_category.delete()
        self.test_author.delete()

    def test_articles_count_normal_case(self):
        self.assertEqual(self.articles_count, self.test_category.articles_count())
