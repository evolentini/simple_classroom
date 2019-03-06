# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_dropbox.storage


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0012_auto_20150409_0140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'ordering': ['-dictation__year', 'title'], 'verbose_name': 'Asignaci\xf3n', 'verbose_name_plural': 'Asignaciones'},
        ),
        migrations.AlterField(
            model_name='assignment',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Tildar para mostrar la asignaci\xf3n a los inscriptos en el dictado seleccionado.', verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='avatar',
            field=models.ImageField(storage=django_dropbox.storage.DropboxStorage(location=b'/simple_classroom'), upload_to=b'avatar', null=True, verbose_name='Avatar', blank=True),
        ),
    ]
