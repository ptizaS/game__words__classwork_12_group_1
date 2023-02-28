from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.backends.cached_db import SessionStore
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from apps.game.models import Word, Room


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
    success_url = reverse_lazy("game:create")
    
    
class RoomCreate(TemplateView):
    model = Room
    
    fields = (
        "room_number",
        "main_player",
        "other_player",
    )

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session

        context = super().get_context_data(**kwargs)
        context["session_id"] = session.session_key
        return context
