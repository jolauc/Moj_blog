# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Nazwa Kategorii', max_length=100)),
                ('slug', models.SlugField(verbose_name='Odnośnik', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Tytuł', max_length=255)),
                ('slug', models.SlugField(verbose_name='Odnośnik', max_length=255, unique=True)),
                ('text', models.TextField(verbose_name='Treść')),
                ('posted_date', models.DateTimeField(verbose_name='Data dodania', auto_now_add=True)),
                ('categories', models.ManyToManyField(verbose_name='Kategorie', to='news.Category')),
            ],
            options={
                'verbose_name': 'Wiadomość',
                'verbose_name_plural': 'Wiadomości',
            },
        ),
    ]
