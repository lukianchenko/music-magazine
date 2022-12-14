# Generated by Django 3.2.13 on 2022-10-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20220705_1754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.ImageField(default='default.png', upload_to='covers'),
        ),
    ]
