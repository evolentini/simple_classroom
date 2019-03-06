# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['order'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AddField(
            model_name='book',
            name='comments',
            field=models.CharField(max_length=255, null=True, verbose_name='Comentarios', blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='order',
            field=models.IntegerField(null=True, verbose_name='Orden', blank=True),
        ),
    ]
