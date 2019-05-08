from django.db import transaction
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, \
    ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from api import schemas
from api import serializers
from blog.utils import MultipartMixin, FilterQuerysetMixin, schema_method_decorator as smd, OrderingMixin
from main.models import Post, Comment, Tag, Profile
from main.permissions import CommentDetailPermission, PostDetailPermission, ProfileUpdatePermission
from django_filters import rest_framework as filters

DEFAULT_PERMS = api_settings.DEFAULT_PERMISSION_CLASSES


@smd('post', operation_summary='Sign up')
@method_decorator(transaction.atomic, 'post')
class SignUpView(MultipartMixin, CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.SingUpSerializer

    # @transaction.atomic
    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)


@smd('post', operation_summary='Sign in', responses=schemas.sign_in)
class SignInView(JSONWebTokenAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = JSONWebTokenSerializer


class PostFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title']


class PostView(MultipartMixin, ListCreateAPIView):
    queryset = Post.objects.annotate(comments_count=Count('comments')).order_by('-created_at')
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)


class PostDetailView(MultipartMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, PostDetailPermission)
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    lookup_url_kwarg = 'id'


class CommentView(FilterQuerysetMixin, OrderingMixin, ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    ordering_fields = ('pk',)
    filter_kwargs = {'post_id': 'id'}

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['id'])
        serializer.save(author_id=self.request.user.pk, post=post)

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).filter(post_id=self.kwargs['id'])


class CommentDetailView(FilterQuerysetMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, CommentDetailPermission)
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer
    lookup_url_kwarg = 'comment_id'

    filter_kwargs = {'post_id': 'id'}

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).filter(post_id=self.kwargs['id'])


class TagView(OrderingMixin, ListAPIView):
    queryset = Tag.objects.annotate(posts_count=Count('posts'))
    serializer_class = serializers.TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    ordering_fields = ('pk',)


@method_decorator(never_cache, 'get')
class TagPostsView(FilterQuerysetMixin, OrderingMixin, ListAPIView):
    pagination_class = None
    queryset = Post.objects.annotate(comments_count=Count('comments'))
    serializer_class = serializers.TagPostsSerializer
    permission_classes = ()

    filter_kwargs = {'tags__pk': 'id'}
    ordering_fields = ('pk',)

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).filter(tags__pk=self.kwargs['id'])


class ProfileView(ListAPIView):
    serializer_class = serializers.ProfileSerializer
    permission_classes = ()

    def get_queryset(self):
        return Profile.objects.annotate(
            posts_count=Count('posts'),
            comments_count=Count('comments'),
        ).order_by('user__email')

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).exclude(pk=self.request.user.pk)


class ProfileDetailView(MultipartMixin, RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileDetailSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly, ProfileUpdatePermission)


class ProfilePostView(FilterQuerysetMixin, OrderingMixin, ListAPIView):
    queryset = Post.objects.annotate(comments_count=Count('comments'))
    serializer_class = serializers.ProfilePostSerializer

    filter_kwargs = {'author_id': 'id'}
    ordering_fields = ('-created_at',)
