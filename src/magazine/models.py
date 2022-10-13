from tabnanny import verbose
import uuid as uuid

from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_datetime = models.DateTimeField(null=True, auto_now_add=True)
    last_update = models.DateTimeField(null=True, auto_now=True)


class Article(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True)
    category = models.ForeignKey(to="magazine.Category", related_name="articles", on_delete=models.CASCADE)
    author = models.ForeignKey(to=get_user_model(), related_name="articles", on_delete=models.CASCADE)
    cover_image = models.ImageField(default="default.png", upload_to="covers")
    title = models.CharField(max_length=1024)
    text = models.TextField()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def articles_count(self):
        return self.articles.count()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ArticleTag(BaseModel):
    article = models.ForeignKey(to="magazine.Article", related_name="article_tags", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="magazine.Tag", related_name="article_tags", on_delete=models.CASCADE)
