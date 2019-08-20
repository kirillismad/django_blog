from django.db import transaction
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, \
    ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from api import schemas
from api import serializers
from blog.utils import MultipartMixin, schema_method_decorator as smd
from blog.utils import PathKwargsFilterBackend
from main.models import Post, Comment, Tag, Profile
from main.permissions import CommentDetailPermission, PostDetailPermission, ProfileUpdatePermission


@smd('post', operation_summary='Sign up', security=[])
@method_decorator(transaction.atomic, 'post')
class SignUpView(MultipartMixin, CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.SingUpSerializer


@smd('post', operation_summary='Sign in', responses=schemas.sign_in, security=[])
class SignInView(JSONWebTokenAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = JSONWebTokenSerializer


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        fields = ['title']


@smd('get', operation_summary='Retrieve list of posts', security=[])
@smd('post', operation_summary='Create post')
class PostView(MultipartMixin, ListCreateAPIView):
    queryset = Post.objects.annotate(comments_count=Count('comments')).order_by('-created_at')
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)


@smd('get', operation_summary='Retrieve specific post', security=[])
@smd('put', operation_summary='Update specific post')
@smd('patch', operation_summary='Partial update specific post')
@smd('delete', operation_summary='Delete specific post')
class PostDetailView(MultipartMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, PostDetailPermission)
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    lookup_url_kwarg = 'id'


@smd('get', operation_summary='Retrieve list of comments', security=[])
@smd('post', operation_summary='Create comment')
class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [PathKwargsFilterBackend, OrderingFilter]
    filter_kwargs = {'post_id': 'id'}
    ordering_fields = ['pk', 'created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['id'])
        serializer.save(author_id=self.request.user.pk, post=post)


@smd('get', operation_summary='Retrieve specific comment', security=[])
@smd('put', operation_summary='Update specific comment')
@smd('patch', operation_summary='Partial update specific comment')
@smd('delete', operation_summary='Delete specific comment')
class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, CommentDetailPermission)
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer
    lookup_url_kwarg = 'comment_id'

    filter_backends = [PathKwargsFilterBackend]
    filter_kwargs = {'post_id': 'id'}


@smd('get', operation_summary='Retrieve list of tags', security=[])
class TagView(ListAPIView):
    queryset = Tag.objects.annotate(posts_count=Count('posts'))
    serializer_class = serializers.TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [OrderingFilter]
    ordering = ['title']
    ordering_fields = ['pk', 'title']


@smd('get', operation_summary='Retrieve list of posts for specific tag', security=[])
@method_decorator(never_cache, 'get')
class TagPostsView(ListAPIView):
    pagination_class = None
    queryset = Post.objects.annotate(comments_count=Count('comments'))
    serializer_class = serializers.TagPostsSerializer
    permission_classes = ()

    filter_backends = [PathKwargsFilterBackend, OrderingFilter]
    filter_kwargs = {'tags__pk': 'id'}

    ordering = ['title']
    ordering_fields = ['pk', 'title', 'created_at']


@smd('get', operation_summary='Retrieve list of profiles', security=[])
class ProfileView(ListAPIView):
    serializer_class = serializers.ProfileSerializer
    permission_classes = ()

    def get_queryset(self):
        return Profile.objects.annotate(
            posts_count=Count('posts'),
            comments_count=Count('comments'),
        ).order_by('user__email')


@smd('get', operation_summary='Retrieve specific profile', security=[])
@smd('put', operation_summary='Update own profile')
@smd('patch', operation_summary='Partial update own profile')
class ProfileDetailView(MultipartMixin, RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileDetailSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly, ProfileUpdatePermission)


@smd('get', operation_summary='Retrieve list of posts for specific profile', security=[])
class ProfilePostView(ListAPIView):
    queryset = Post.objects.annotate(comments_count=Count('comments'))
    serializer_class = serializers.ProfilePostSerializer
    permission_classes = ()

    filter_backends = [PathKwargsFilterBackend, OrderingFilter]
    filter_kwargs = {'author_id': 'id'}

    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
