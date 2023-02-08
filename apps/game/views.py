
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.game.models import Word


class WordListView(ListView):
    model = Word

def index(request):
    return render(
        request=request,
        template_name="index.html",
    )

class WordCreateView(CreateView):
    model = Word

    fields = (
        "word",
    )
    success_url = reverse_lazy("game:list")


