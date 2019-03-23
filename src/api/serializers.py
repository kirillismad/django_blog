from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import get_error_detail

from api.validators import validate_password_pair
from main.models import Profile, User, Post, Tag, Comment


class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs.setdefault('write_only', True)
        kwargs.setdefault('min_length', 8)
        kwargs.setdefault('max_length', 128)
        super().__init__(**kwargs)


class SingUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    password = PasswordField(source='user.password')
    confirm_password = PasswordField(source='user.confirm_password')

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar', 'email', 'password', 'confirm_password', 'wallpaper')

    def validate(self, attrs):
        user_kwargs = attrs.pop('user')

        password_confirmation = user_kwargs.pop('confirm_password')
        validate_password_pair(user_kwargs['password'], password_confirmation)

        user = User.objects.create_user(commit=False, **user_kwargs)
        try:
            user.full_clean()
        except DjangoValidationError as e:
            raise ValidationError(get_error_detail(e), 'user_validation_error')

        return {'user': user, **attrs}

    def create(self, validated_data):
        user = validated_data.pop('user')
        user.save()
        return Profile.objects.create(user=user, **validated_data)


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
        fields = ('id', 'author_id', 'message')


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
    class Meta:
        model = Profile
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar')
        extra_kwargs = {
            'id': {'source': 'pk'},
            'email': {'source': 'user.email', 'read_only': True}
        }


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'avatar', 'wallpaper')
        extra_kwargs = {
            'email': {'source': 'user.email'}
        }


class ProfileSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email' 'first_name', 'last_name', 'avatar', 'wallpaper')
        extra_kwargs = {
            'id': {'source': 'pk'},
            'email': {'source': 'user.email', 'read_only': True}
        }


class ProfilePostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'created_at', 'tags', 'comments_count')
