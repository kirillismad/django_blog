from uuid import uuid4

from django.utils.deconstruct import deconstructible
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.settings import api_settings


@deconstructible
class UploadToFactory:
    extensions = ('tar.gz',)

    def __init__(self, path=None):
        self.path = path

    def __call__(self, instance, filename):
        path = self.get_path(instance)
        ext = self.get_extension(filename)

        return '{path}/{filename}.{extension}'.format(path=path, filename=uuid4().hex, extension=ext)

    def get_extension(self, filename):
        for ext in self.extensions:
            if filename.endswith(ext):
                return ext
        return filename.rsplit('.', 1)[-1]

    def get_path(self, instance):
        if self.path is None:
            raise ValueError(f'Override {self.__class__.__name__}.`get_path` or pass `path` in constructor')
        return self.path


class MultipartMixin:
    multipart_parser = MultiPartParser
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES + [multipart_parser]

    @property
    def is_fake(self):
        return getattr(self, 'swagger_fake_view', False)

    def get_parsers(self):
        if self.is_fake:
            return [self.multipart_parser]
        return super().get_parsers()

    def get_serializer_context(self):
        return {
            'is_fake': self.is_fake,
            **super().get_serializer_context()
        }


class FilterQuerysetMixin:
    filter_kwargs = {}

    def filter_queryset(self, queryset):
        filter_kwargs = {
            lookup: self.kwargs[kwarg]
            for lookup, kwarg in
            self.filter_kwargs.items()
        }
        return super().filter_queryset(queryset).filter(**filter_kwargs)


class OrderingMixin:
    ordering_fields = ()

    def get_queryset(self):
        return super().get_queryset().order_by(*self.ordering_fields)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'id': user.pk
    }


def schema_method_decorator(name, **kwargs):
    def wrapper(cls):
        return method_decorator(decorator=swagger_auto_schema(**kwargs), name=name)(cls)

    return wrapper
