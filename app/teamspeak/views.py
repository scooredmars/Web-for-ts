from django.utils import timezone
from django.views.generic import ListView

from .models import Post


class PostList(ListView):

    template_name = 'teamspeak/home.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('published_date')
