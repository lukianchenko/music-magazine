import uuid as uuid

from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True)
    category = models.ForeignKey(to="magazine.Category", related_name="articles", on_delete=models.CASCADE)
    author = models.ForeignKey(to=get_user_model(), related_name="articles", on_delete=models.CASCADE)
    cover_image = models.ImageField(default="default.png", upload_to="media/covers")
    title = models.CharField(max_length=1024)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def articles_count(self):
        return self.articles.count()


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    article = models.ForeignKey(to="magazine.Article", related_name="article_tags", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="magazine.Tag", related_name="article_tags", on_delete=models.CASCADE)
