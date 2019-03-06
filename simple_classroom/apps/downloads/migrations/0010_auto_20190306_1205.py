# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_dropbox.storage
import simple_classroom.apps.downloads.models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0009_auto_20150409_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='data',
            field=models.FileField(storage=django_dropbox.storage.DropboxStorage(location=b'/simple_classroom'), null=True, upload_to=b'files', blank=True),
        ),
        migrations.AlterField(
            model_name='sitedownload',
            name='data',
            field=models.FileField(storage=django_dropbox.storage.DropboxStorage(location=b'/simple_classroom'), null=True, upload_to=simple_classroom.apps.downloads.models.get_upload_path, blank=True),
        ),
    ]
