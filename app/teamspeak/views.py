from django.views.generic import ListView

from .models import Home


class HomeList(ListView):

    template_name = 'teamspeak/home.html'
    model = Home
    context_object_name = 'home'
