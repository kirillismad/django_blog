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
from django.views.generic.edit import FormMixin

from main.forms import SignUpForm, SignInForm, CommentForm, ProfileUpdateForm, PostForm
from main.models import Post, Profile, Tag, Comment


class MainView(generic.ListView):
    template_name = 'main/main.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # TODO add search filter
        qs = Post.objects.select_related('author').prefetch_related('tags')
        qs = qs.annotate(comments_count=Count('comments'))
        return qs


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
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.select_related('author').prefetch_related(
            'tags', Prefetch('comments', Comment.objects.select_related('author').order_by('-created_at'))
        )

    def get_context_data(self, **kwargs):
        return {'form': CommentForm(), **super().get_context_data(**kwargs)}


class CommentView(LoginRequiredMixin, FormMixin, View):
    login_url = reverse_lazy('main:sign_in')
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['id'])
        form = self.get_form()
        if form.is_valid():
            form.instance.post = post
            form.instance.author_id = request.user.pk
            form.save()
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
        return Profile.objects.prefetch_related(
            Prefetch('posts', Post.objects.annotate(comments_count=Count('comments')))
        )


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
