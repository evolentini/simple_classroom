# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_dropbox.storage


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0013_auto_20190306_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=255, verbose_name='Autor')),
                ('edition', models.CharField(max_length=255, verbose_name='Edici\xf3n')),
                ('editorial', models.CharField(max_length=255, verbose_name='Editorial')),
                ('cover_image', models.ImageField(storage=django_dropbox.storage.DropboxStorage(location=b'/simple_classroom'), upload_to=b'books', null=True, verbose_name='Imagen', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='Titulo')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='GroupCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('order', models.IntegerField(verbose_name='Orden')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(to='bibliography.GroupCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(to='classroom.Subject'),
        ),
    ]
