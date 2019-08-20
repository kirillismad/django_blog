from random import choice, sample
from string import ascii_lowercase, ascii_letters, digits

from blog.tests_utils.utils import patch_storage
from main.models import User, Profile, Tag, Post, Comment


class MainFactory:
    def __init__(self, primitive_factory):
        self.primitive_factory = primitive_factory

    def get_email(self) -> str:
        existed = set(User.objects.all().values_list('email', flat=True))
        while True:
            email = self._get_email()
            if email not in existed:
                return email

    def _get_email(self) -> str:
        pattern = '{base}@{domain}'
        domains = ('gmail.com', 'yandex.ru', 'mail.ru', 'list.ru', 'rofl.com')
        return pattern.format(base=self.primitive_factory.get_string(alphabet=ascii_lowercase), domain=choice(domains))

    def get_password(self) -> str:
        return self.primitive_factory.get_string(16, alphabet=ascii_letters + digits)

    def get_name(self) -> str:
        return self.primitive_factory.get_string(alphabet=ascii_lowercase).capitalize()

    def get_user(self, **kwargs) -> User:
        kwargs.setdefault('email', self.get_email())
        kwargs.setdefault('password', self.get_password())

        return User.objects.create_user(**kwargs)

    @patch_storage
    def get_profile(self, **kwargs) -> Profile:
        if 'user' not in kwargs:
            kwargs['user'] = self.get_user()

        kwargs.setdefault('first_name', self.get_name())
        kwargs.setdefault('last_name', self.get_name())
        kwargs.setdefault('wallpaper', self.primitive_factory.get_image_file())
        kwargs.setdefault('avatar', self.primitive_factory.get_image_file())

        return Profile.objects.create(**kwargs)

    @patch_storage
    def get_post(self, tags_count=None, **kwargs):
        if 'author' not in kwargs:
            kwargs['author'] = self.get_profile()
        kwargs.setdefault('title', self.primitive_factory.get_title())
        kwargs.setdefault('image', self.primitive_factory.get_image_file())
        kwargs.setdefault('text', self.primitive_factory.get_text(7))

        post = Post.objects.create(**kwargs)

        if tags_count is not None:
            tags = self._get_tags(tags_count)
            post.tags.set(tags)

        return post

    def _get_tags(self, count):
        tags = list(Tag.objects.all())
        for _ in range(count + 2 - len(tags)):
            tags.append(self.get_tag())

        return sample(tags, count)

    def get_comment(self, **kwargs):
        if 'author' not in kwargs:
            kwargs['author'] = self.get_profile()
        if 'post' not in kwargs:
            kwargs['post'] = self.get_post()

        kwargs.setdefault('message', self.primitive_factory.get_text(10))
        return Comment.objects.create(**kwargs)

    def get_tag(self, **kwargs):
        kwargs.setdefault('title', self.primitive_factory.get_title())
        return Tag.objects.create(**kwargs)
