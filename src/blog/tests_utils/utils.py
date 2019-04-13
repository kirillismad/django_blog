from unittest.mock import MagicMock, patch

from django.core.files import File


def patch_storage(func):
    def new_save(name, *args, **kwargs):
        return name

    return patch('django.core.files.storage.FileSystemStorage.save', MagicMock(side_effect=new_save))(func)


def patch_file(func):
    return patch('django.core.files.File', MagicMock(File))(func)
