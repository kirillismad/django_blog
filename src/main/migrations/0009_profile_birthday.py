# Generated by Django 2.1.7 on 2019-04-15 05:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190414_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 4, 15, 5, 57, 59, 611924, tzinfo=utc), verbose_name='birthday date'),
            preserve_default=False,
        ),
    ]
