from django.db import transaction
from django.db.models import Count, Max
from django.utils.decorators import method_decorator
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, \
    ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from api import serializers
from blog.utils import MultipartMixin, FilterQuerysetMixin, ExcludeSelfMixin
from main.models import Post, Comment, Tag, Profile
from main.permissions import CommentDetailPermission, PostDetailPermission

DEFAULT_PERMS = api_settings.DEFAULT_PERMISSION_CLASSES


@method_decorator(transaction.atomic, 'post')
class SignUpView(MultipartMixin, CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SingUpSerializer

    # @transaction.atomic
    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)


class SignInView(JSONWebTokenAPIView):
    permission_classes = (AllowAny,)
    serializer_class = JSONWebTokenSerializer


class PostView(MultipartMixin, ListCreateAPIView):
    queryset = Post.objects.annotate(comments_count=Count('comments')).order_by('-created_at')
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)


class PostDetailView(MultipartMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = DEFAULT_PERMS + [PostDetailPermission]
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    lookup_url_kwarg = 'id'


class CommentView(FilterQuerysetMixin, ListCreateAPIView):
    queryset = Comment.objects.order_by('pk')
    serializer_class = serializers.CommentSerializer

    filter_kwargs = {'post_id': 'id'}

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['id'])
        serializer.save(author_id=self.request.user.pk, post=post)

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).filter(post_id=self.kwargs['id'])


class CommentDetailView(FilterQuerysetMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = DEFAULT_PERMS + [CommentDetailPermission]
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer
    lookup_url_kwarg = 'comment_id'

    filter_kwargs = {'post_id': 'id'}

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).filter(post_id=self.kwargs['id'])


class TagView(ListAPIView):
    queryset = Tag.objects.annotate(posts_count=Count('posts')).order_by('pk')
    serializer_class = serializers.TagSerializer


class TagPostsView(FilterQuerysetMixin, ListAPIView):
    queryset = Post.objects.all().order_by('pk')
    serializer_class = serializers.PostSerializer

    filter_kwargs = {'tags__pk': 'id'}

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).filter(tags__pk=self.kwargs['id'])


class ProfileView(ExcludeSelfMixin, ListAPIView):
    serializer_class = serializers.ProfileSerializer

    def get_queryset(self):
        # TODO
        return Profile.objects.annotate(
            posts_count=Count('posts'),
            comments_count=Count('comments'),
            # favorite_tag= . . .
        ).order_by('user__email')

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).exclude(pk=self.request.user.pk)


class ProfileDetailView(ExcludeSelfMixin, RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileDetailSerializer
    lookup_url_kwarg = 'id'

    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset).exclude(pk=self.request.user.pk)


class ProfilePostView(FilterQuerysetMixin, ListAPIView):
    queryset = Post.objects.annotate(comments_count=Count('comments')).order_by('-created_at')
    serializer_class = serializers.ProfilePostSerializer
    filter_kwargs = {'author_id': 'id'}


class ProfileSelfView(MultipartMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProfileSelfSerializer

    def get_object(self):
        return self.request.user.profile
