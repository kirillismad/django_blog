import os
import re
from functools import partial

from django.conf import settings
from django.test import override_settings
from django.urls import reverse
from django.utils.functional import cached_property
from rest_framework.test import APITestCase

from blog.tests_utils.main_factory import MainFactory
from blog.tests_utils.primitive_factory import PrimitiveFactory
from pprint import pformat


class TestCaseMeta(type):
    def __new__(mcs, name, bases, attrs):
        result = super().__new__(name, bases, attrs)
        return override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_media'))(result)


class BaseTestCase(APITestCase, metaclass=TestCaseMeta):
    regexp = re.compile(r'^assert(?P<code>\d{3})$')
    codes = (200, 201, 204) + (403,)
    VIEW = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.primitive_factory = PrimitiveFactory()
        cls.main_factory = MainFactory(cls.primitive_factory)

    def assertStatus(self, status_code, response):
        message = None if not response.content else pformat(response.json())
        self.assertEqual(status_code, response.status_code, message)

    def __getattr__(self, item):
        match = self.regexp.match(item)
        if match:
            code = int(match.group('code'))
            if code in self.codes:
                return partial(self.assertStatus, code)
            msg = 'Invalid status code. Available status_codes: {}'.format(', '.join(map(str, self.codes)))
            raise ValueError(msg)

        msg = f'{self.__class__.__name__} object has no attribute {item}'
        raise AttributeError(msg)

    def get_reverse_kwargs(self):
        return {}

    @cached_property
    def url(self):
        return reverse(self.VIEW, kwargs=self.get_reverse_kwargs())


class ProfileAPITestCase(BaseTestCase):
    def get_user(self):
        return self.main_factory.get_user()

    def get_profile(self):
        return self.main_factory.get_profile(user=self.get_user())

    def setUp(self):
        self.profile = self.get_profile()
        self.client.force_authenticate(user=self.profile.user)
