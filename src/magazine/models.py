import uuid as uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    visible = models.BooleanField(default=False)
    tags = models.ManyToManyField(to="magazine.Tag", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=128)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def articles_count(self):
        return self.articles.count()

    def html_class_name(self):
        return self.name.lower().replace(" ", "")

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Tag(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
