from functools import wraps

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Prefetch, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View, generic

from main.forms import SignUpForm, SignInForm, CommentForm, PostForm, ProfileUpdateForm
from main.models import Post, Profile, Tag, Comment


def method_login_required(method):
    @wraps(method)
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('main:sign_in')
        return method(self, request, *args, **kwargs)

    return wrapper


class MainView(View):
    def get(self, request):
        posts = Post.objects.select_related('author').prefetch_related('tags') \
            .annotate(comments_count=Count('comments')).order_by('-created_at')

        q = request.GET.get('q')
        if q is not None:
            posts = posts.filter(Q(text__search=q) | Q(title__icontains=q))

        return render(request, 'main/main.html', {'posts': posts, 'user': request.user, 'form': PostForm()})

    @method_login_required
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.pk
            post.save()
            form.save_m2m()
            return redirect(post)
        return redirect('main:root')


class PostDetailView(generic.DetailView):
    pk_url_kwarg = 'id'
    template_name = 'main/post_detail.html'

    def get_queryset(self):
        pfr_comments = Prefetch('comments', Comment.objects.select_related('author').order_by('-created_at'))
        return Post.objects.select_related('author').prefetch_related('tags', pfr_comments)

    def get_context_data(self, **kwargs):
        return {
            'post': self.object,
            'user': self.request.user,
            'form': CommentForm()
        }

    # def get(self, request, id):
    #     form = CommentForm()
    #     pfr_comments = Prefetch('comments', Comment.objects.select_related('author').order_by('-created_at'))
    #     post = get_object_or_404(Post.objects.select_related('author').prefetch_related('tags', pfr_comments), pk=id)
    #     return render(request, 'main/post_detail.html', context={'post': post, 'user': request.user, 'form': form})


class CommentView(View):
    @method_login_required
    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author_id = request.user.pk
            comment.save()
        return redirect(post)


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'main/sign_up.html', context={'form': form, 'user': request.user})

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save()
            login(request, profile.user)
            return redirect(reverse('main:root'))

        return render(request, 'main/sign_up.html', context={'form': form, 'user': request.user})


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'main/sign_in.html', context={'form': form, 'user': request.user})

    def post(self, request):
        form = SignInForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']

            login(request, user)
            return redirect(reverse('main:root'))
        return render(request, 'main/sign_in.html', context={'form': form, 'user': request.user})


class SingOut(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('main:root'))


# @method_decorator(cache_page(60 * 3), 'get')
class ProfileView(generic.ListView):
    queryset = Profile.objects.annotate(posts_count=Count('posts'))
    template_name = 'main/profiles.html'

    def get_queryset(self):
        profiles = super().get_queryset()
        q = self.request.GET.get('q')
        if q is not None:
            profiles = profiles.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))

        return profiles

    def get_context_data(self, *args, **kwargs):
        return {
            'profiles': self.object_list, 'user': self.request.user
        }

    # def get(self, request):
    #     profiles = Profile.objects.annotate(posts_count=Count('posts'))
    #
    #     q = request.GET.get('q')
    #     if q is not None:
    #         profiles = profiles.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
    #     return render(request, 'main/profiles.html', context={'profiles': profiles, 'user': request.user})


class ProfileDetailView(generic.DetailView):
    template_name = 'main/profile_detail.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        pfr_posts = Prefetch('posts', Post.objects.annotate(comments_count=Count('comments')))
        return Profile.objects.prefetch_related(pfr_posts)

    def get_context_data(self, **kwargs):
        return {'profile': self.object, 'user': self.request.user}

    # def get(self, request, id):
    #     pfr_posts = Prefetch('posts', Post.objects.annotate(comments_count=Count('comments')))
    #     profile = get_object_or_404(Profile.objects.prefetch_related(pfr_posts), pk=id)
    #
    #     return render(request, 'main/profile_detail.html', context={'profile': profile, 'user': request.user})


@method_decorator(login_required, 'dispatch')
class ProfileUpdateView(View):
    def get(self, request, id):
        profile = get_object_or_404(Profile, pk=id)
        if request.user.pk != profile.pk:
            raise PermissionDenied()

        form = ProfileUpdateForm(instance=profile)

        return render(request, 'main/profile_update.html', context={'form': form, 'user': request.user})

    def post(self, request, id):
        profile = get_object_or_404(Profile, pk=id)
        if request.user.pk != profile.pk:
            raise PermissionDenied()

        form = ProfileUpdateForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(profile)
        return render(request, 'main/profile_update.html', context={'form': form, 'user': request.user})


class TagsView(generic.ListView):
    queryset = Tag.objects.all()
    template_name = 'main/tags.html'

    # def get(self, request):
    #     tags = Tag.objects.all()
    #     return render(request, 'main/tags.html', context={'tags': tags, 'user': request.user})

    def get_context_data(self, *args, **kwargs):
        return {'tags': self.object_list, 'user': self.request.user}


@method_decorator(login_required, 'dispatch')
class ProfileSelfView(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('main:profiles_detail', kwargs={'id': self.request.user.pk})

    # def get(self, request):
    #     return redirect('main:profiles_detail', id=request.user.pk)
