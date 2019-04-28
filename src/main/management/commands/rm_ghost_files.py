import os

from django.core.management import BaseCommand
from django.conf import settings

from main.models import Profile, Post
from os.path import join


def get_files(model, field, path):
    file_dir = join(settings.MEDIA_ROOT, path)
    actual_files = set(map(lambda f: join(settings.MEDIA_ROOT, f), model.objects.values_list(field, flat=True)))
    all_files = set(map(lambda f: join(file_dir, f), os.listdir(file_dir)))

    return all_files - actual_files


def rm_files(model, field, path):
    for file in get_files(model, field, path):
        os.remove(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        rm_files(Profile, 'avatar', 'main/profile/avatar')
        rm_files(Profile, 'wallpaper', 'main/profile/wallpaper')
        rm_files(Post, 'image', 'main/post/image')
