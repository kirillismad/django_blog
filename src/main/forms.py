from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from main.models import Profile, User, Comment, Post, Tag


class SignUpForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
    )

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar', 'email', 'password', 'confirm_password', 'wallpaper', 'birthday')

    def clean(self):
        user_fields = ('email', 'password', 'confirm_password')
        user_data = {f: self.cleaned_data.pop(f) for f in user_fields}

        try:
            validate_password(user_data['password'])
        except ValidationError as e:
            self.add_error('password', e)

        confirm_password = user_data.pop('confirm_password')
        if user_data['password'] != confirm_password:
            self.add_error(
                'confirm_password',
                ValidationError(_("The two password fields didn't match."), 'password_mismatch')
            )

        user = User(email=user_data['email'])

        try:
            user.validate_unique()
        except ValidationError as e:
            for field, er in e.error_dict.items():
                self.add_error(field, er)
        return {'user': user_data, **self.cleaned_data}

    def _post_clean(self):
        pass

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data.pop('user'))
        self.instance = Profile(user=user, **self.cleaned_data)

        if commit:
            self.instance.save()

        return self.instance


class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
    )

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = authenticate(email=email, password=password)

        if user is None:
            raise ValidationError(_('There is no user with such credentials'), 'invalid_credentials')

        return {'user': user}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'image', 'text', 'tags')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
