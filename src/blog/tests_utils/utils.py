from unittest.mock import MagicMock, patch

from django.core.files import File

FILE_MOCK = MagicMock(File, name='FileMock')


def new_save(*args, **kwargs):
    return args[1]


def patch_storage(func):
    return patch(
        'django.core.files.storage.FileSystemStorage.save',
        new=new_save
    )(func)


def patch_file(func):
    return patch('django.core.files.File', FILE_MOCK)(func)
