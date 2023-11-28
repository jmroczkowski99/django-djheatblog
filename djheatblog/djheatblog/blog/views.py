from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 4

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


class PostView(DetailView):
    model = Post
    context_object_name = "single_post"
    template_name = "blog/single.html"
