from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.views import generic

from main.models import Post


class MainView(View):
    def get(self, request):
        posts = Post.objects.annotate(comments_count=Count('comments'))

        return render(request, 'main/main.html', {'posts': posts, 'user': request.user})
