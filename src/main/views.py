from django.contrib.auth import login
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from main.forms import SignUpForm

from main.models import Post


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
