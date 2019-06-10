import base64

from django.core.files.base import ContentFile
from drf_writable_nested import UniqueFieldsMixin, NestedCreateMixin
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from api.validators import validate_password_pair
from main.models import Profile, User, Post, Tag, Comment


class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs.setdefault('write_only', True)
        kwargs.setdefault('min_length', 8)
        kwargs.setdefault('max_length', 128)
        super().__init__(**kwargs)


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str):
            data = ContentFile(base64.b64decode(data), name='temp.png')

        return super().to_internal_value(data)


class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    confirm_password = PasswordField()
    password = PasswordField()

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs['password']
        validate_password_pair(password, confirm_password)

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SingUpSerializer(NestedCreateMixin, serializers.ModelSerializer):
    user = UserSerializer()
    avatar = Base64ImageField()
    wallpaper = Base64ImageField()

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'avatar', 'wallpaper', 'birthday')


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'author_id', 'tags', 'title', 'image', 'text', 'created_at', 'comments_count')
        extra_kwargs = {
            'image': {'write_only': True},
            'text': {'write_only': True},
        }


class PostDetailSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('author_id', 'tags', 'title', 'image', 'text', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_id', 'message', 'created_at')


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author_id', 'message')


class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'title', 'posts_count')


class ProfileSerializer(serializers.ModelSerializer):
    posts_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar', 'posts_count', 'comments_count')
        extra_kwargs = {
            'id': {'source': 'pk'},
            'email': {'read_only': True}
        }


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'avatar', 'wallpaper')
        extra_kwargs = {
            'email': {'read_only': True}
        }


class ProfileSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar', 'wallpaper')
        extra_kwargs = {
            'id': {'source': 'pk', 'read_only': True},
            'email': {'read_only': True}
        }


class ProfilePostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'created_at', 'tags', 'comments_count')


class TagPostAuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)
    source_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'full_name', 'source_url')
        extra_kwargs = {
            'id': {'source': 'pk'}
        }

    @swagger_serializer_method(serializer_or_field=serializers.CharField)
    def get_source_url(self, profile):
        return profile.get_absolute_url()


class TagPostsSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)
    author = TagPostAuthorSerializer(read_only=True)
    tags = serializers.SlugRelatedField('title', many=True, read_only=True)
    source_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'created_at', 'tags', 'comments_count', 'author', 'image', 'source_url')

    @swagger_serializer_method(serializer_or_field=serializers.CharField)
    def get_source_url(self, post):
        return post.get_absolute_url()
