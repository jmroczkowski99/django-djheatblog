from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Q

from .models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 4

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest = self.get_latest_post()
        context['latest'] = latest
        return context

    def get_latest_post(self):
        return Post.objects.latest("updated_at")


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(request, "blog/single.html", {"post": post, "related": related})


def tags(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, "blog/tag.html", {"tag": tag, "posts": posts})


class SearchResultsView(ListView):
    model = Post
    context_object_name = "search"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(content__icontains=query)
        )
        return object_list
