from django.urls import path

from movies.apps import MoviesConfig
from movies.views import MovieListView

app_name = MoviesConfig.name

urlpatterns = [
    path('', MovieListView.as_view(), name='index'),
]