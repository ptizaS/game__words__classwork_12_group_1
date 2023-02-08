from django.urls import path, include

from . import views

app_name = "game"

urlpatterns = [
    path(
        "word/",
        include(
            [
                path("list/", views.WordListView.as_view(), name="list"),
                path("create/", views.WordCreateView.as_view(), name="create"),
            ]
        ),
    ),

]