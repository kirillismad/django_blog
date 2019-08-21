from functools import wraps

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.views.decorators.cache import never_cache

from main.forms import SignUpForm, SignInForm, CommentForm, ProfileUpdateForm, PostForm
from main.models import Post, Profile, Tag, Comment


def method_login_required(method):
    @wraps(method)
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('main:sign_in')
        return method(self, request, *args, **kwargs)

    return wrapper


class MainView(generic.ListView):
    template_name = 'main/main.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # TODO add search filter
        return Post.objects.select_related('author').prefetch_related('tags') \
            .annotate(comments_count=Count('comments')).order_by('-created_at')


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('main:sign_in')

    template_name = 'main/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('main:root')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)


@method_decorator(never_cache, 'get')
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


# TODO add search filter
class ProfileView(generic.ListView):
    queryset = Profile.objects.annotate(posts_count=Count('posts'))
    template_name = 'main/profiles.html'
    context_object_name = 'profiles'


@method_decorator(never_cache, 'get')
class ProfileDetailView(generic.DetailView):
    template_name = 'main/profile_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'profile'

    def get_queryset(self):
        pfr_posts = Prefetch('posts', Post.objects.annotate(comments_count=Count('comments')))
        return Profile.objects.prefetch_related(pfr_posts)


@method_decorator(never_cache, 'get')
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
    template_name = 'main/tags.html'
    model = Tag
    context_object_name = 'tags'


class ProfileSelfView(LoginRequiredMixin, generic.RedirectView):
    login_url = reverse_lazy('main:sign_in')

    def get_redirect_url(self, *args, **kwargs):
        return reverse('main:profiles_detail', kwargs={'id': self.request.user.pk})
