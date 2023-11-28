import factory
from django.contrib.auth.models import User

from djheatblog.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        skip_postgeneration_save = True

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = "published"
    img_url = "test"

    @factory.post_generation
    def tags(self, create, extracted):
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)
    