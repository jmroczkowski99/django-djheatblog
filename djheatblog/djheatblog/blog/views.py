from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import render

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
