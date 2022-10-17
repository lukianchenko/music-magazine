from django.contrib import admin
from django.contrib.auth.models import Group

from magazine.models import (Article, Category, Tag)

for model in (Article, Category, Tag):
    admin.site.register(model)

admin.site.unregister(Group)
