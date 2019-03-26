import re
from functools import partial

from django.urls import reverse
from rest_framework.test import APITestCase

from blog.tests_utils.main_factory import MainFactory
from blog.tests_utils.primitive_factory import PrimitiveFactory
from pprint import pformat


class BaseTestCase(APITestCase):
    regexp = re.compile(r'^assert(?P<code>\d{3})$')
    codes = (200, 201, 204) + (403,)
    VIEW = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.primitive_factory = PrimitiveFactory()
        cls.main_factory = MainFactory(cls.primitive_factory)

    def assertStatus(self, status_code, response):
        message = None if response.content is None else pformat(response.json())
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

    @property
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
