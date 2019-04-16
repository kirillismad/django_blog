from django.contrib.admin import ModelAdmin, register, site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.models import Group
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from main.models import Post, Tag, Comment, User, Profile

site.unregister(Group)


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


@register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (_('Credential info'), {'fields': ('email', 'password')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    form = UserChangeForm

    list_display = ('id', 'email')
    list_filter = ('is_staff',)
    search_fields = ('id', 'email',)
    ordering = ('email',)

    def get_model_perms(self, request):
        return {}


@register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'wallpaper', 'avatar', 'birthday')
    list_display_links = ('pk', 'email', 'first_name', 'last_name', 'birthday')

    ordering = ('user__email', 'first_name', 'last_name')
    search_fields = ('user__email', 'first_name', 'last_name')

    autocomplete_fields = ('user',)


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('pk', 'author', 'title', 'created_at_as_datetime', 'tags_join', 'comments_count')
    list_display_links = list_display

    ordering = ('title',)
    search_fields = ('title', 'author__first_name', 'author__last_name', 'tags__title')

    filter_horizontal = ('tags',)

    list_select_related = ('author',)
    autocomplete_fields = ('author',)

    def tags_join(self, post):
        return ', '.join(post.tags.values_list('title', flat=True))

    tags_join.short_description = _('tags')

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.annotate(comments_count=Count('comments'))

    def comments_count(self, post):
        return post.comments_count

    comments_count.short_description = _('comments')


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = list_display

    ordering = ('title',)
    search_fields = ('title',)


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('pk', 'short_name', 'post_title', 'created_at')
    list_display_links = list_display

    list_select_related = ('author',)

    autocomplete_fields = ('author', 'post')

    def short_name(self, comment):
        return comment.author.short_name

    short_name.short_description = _('full name')

    def post_title(self, comment):
        return comment.post.title

    post_title.short_description = _('post title')
    post_title.admin_order_field = 'post__title'
