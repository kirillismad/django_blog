from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.validators import validate_password_pair
from main.models import Profile, User, Post, Tag, Comment


class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs.setdefault('write_only', True)
        kwargs.setdefault('min_length', 8)
        kwargs.setdefault('max_length', 128)
        super().__init__(**kwargs)


class SingUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        source='user.email',
        validators=[UniqueValidator(User.objects.all(), lookup='iexact')]
    )
    password = PasswordField(source='user.password')
    confirm_password = PasswordField(source='user.confirm_password')

    class Meta:
        model = Profile
        fields = ('email', 'password', 'confirm_password', 'first_name', 'last_name', 'birthday', 'avatar')

    def validate(self, attrs):
        user_data = attrs['user']
        password = user_data['password']
        confirm_password = user_data.pop('confirm_password')
        validate_password_pair(password, confirm_password)

        return attrs

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        return Profile.objects.create(
            user=User.objects.create(**user_data),
            **validated_data
        )


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


class PostHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('url', 'author', 'tags', 'title', 'image', 'text', 'created_at', 'comments_count')
        extra_kwargs = {
            'image': {'write_only': True},
            'text': {'write_only': True},
            'author': {'view_name': 'profiles_detail', 'lookup_url_kwarg': 'id', 'read_only': True},
            'url': {'view_name': 'posts_detail', 'lookup_url_kwarg': 'id', 'read_only': True}
        }


class PostDetailSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('author', 'tags', 'title', 'image', 'text', 'created_at')


class PostDetailHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'tags', 'title', 'image', 'text', 'created_at')
        extra_kwargs = {
            'author': {'view_name': 'profiles_detail', 'lookup_url_kwarg': 'id', 'read_only': True},
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_id', 'message', 'created_at')


class CommentHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'message', 'created_at')
        extra_kwargs = {
            'author': {'view_name': 'profiles_detail', 'lookup_url_kwarg': 'id', 'read_only': True}
        }


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author_id', 'message')


class CommentDetailHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'message')
        extra_kwargs = {
            'author': {'view_name': 'profiles_detail', 'lookup_url_kwarg': 'id', 'read_only': True}
        }


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

    @swagger_serializer_method(serializer_or_field=serializers.URLField)
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

    @swagger_serializer_method(serializer_or_field=serializers.URLField)
    def get_source_url(self, post):
        return post.get_absolute_url()
