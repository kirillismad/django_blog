# Generated by Django 2.1.7 on 2019-04-18 08:54

import blog.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20190418_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=blog.utils.UploadToFactory('main/profile/avatar'), verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallpaper',
            field=models.ImageField(blank=True, null=True, upload_to=blog.utils.UploadToFactory('main/profile/wallpaper'), verbose_name='wallpaper'),
        ),
    ]