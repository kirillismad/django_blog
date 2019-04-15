from django.contrib.admin import AdminSite as BaseAdminSite
from django.contrib.admin.apps import AdminConfig as BaseAdminConfig
from django.utils.translation import gettext_lazy as _


class AdminSite(BaseAdminSite):
    site_header = _('Django blog')
    site_title = _('Django blog site admin')


class AdminConfig(BaseAdminConfig):
    default_site = 'blog.admin.AdminSite'
