from time import time

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import CASCADE
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from blog.utils import UploadToFactory
from main.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)

    is_active = models.BooleanField(_('active status'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Profile(models.Model):
    user = models.OneToOneField(User, CASCADE, primary_key=True, verbose_name=_('user'))
    first_name = models.CharField(_('first_name'), max_length=16, blank=True, db_index=True)
    last_name = models.CharField(_('last_name'), max_length=32, blank=True, db_index=True)
    wallpaper = models.ImageField(_('wallpaper'), upload_to=UploadToFactory('main/profile/wallpaper'), null=True)
    avatar = models.ImageField(_('avatar'), upload_to=UploadToFactory('main/profile/avatar'), null=True)
    birthday = models.DateField(_('birthday date'))

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    @cached_property
    def email(self):
        return self.user.email

    @property
    def short_name(self):
        return f'{self.last_name} {self.first_name[0]}.'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()


class Post(models.Model):
    author = models.ForeignKey(Profile, CASCADE, related_name='posts', verbose_name=_('author'))
    tags = models.ManyToManyField('Tag', related_name='posts', verbose_name=_('tags'))

    title = models.CharField(_('title'), max_length=64, db_index=True)
    image = models.ImageField(_('image'), upload_to=UploadToFactory('main/post/image'))
    text = models.TextField(_('text'))
    created_at = models.IntegerField(_('created at timestamp'), default=time, editable=False, db_index=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class Comment(models.Model):
    author = models.ForeignKey(Profile, CASCADE, related_name='comments', verbose_name=_('author'))
    post = models.ForeignKey(Post, CASCADE, related_name='comments', verbose_name=_('post'))
    message = models.CharField(_('message'), max_length=256)
    created_at = models.DateTimeField(_('created at datetime'), auto_now_add=True)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class Tag(models.Model):
    title = models.CharField(_('title'), max_length=16, unique=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
