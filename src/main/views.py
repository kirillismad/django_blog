from django.contrib.auth import login, logout
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from main.forms import SignUpForm, SignInForm

from main.models import Post, Profile, Tag


class MainView(View):
    def get(self, request):
        posts = Post.objects.annotate(comments_count=Count('comments'))

        return render(request, 'main/main.html', {'posts': posts, 'user': request.user})


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


class ProfileView(View):
    def get(self, request):
        profiles = Profile.objects.annotate(posts_count=Count('posts'))
        return render(request, 'main/profiles.html', context={'profiles': profiles, 'user': request.user})


class TagsView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'main/tags.html', context={'tags': tags, 'user': request.user})
