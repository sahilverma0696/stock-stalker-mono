from django.db import router
from django.urls import path, include
from internal.watchlists.views import WatchListView


urlpatterns = [
    path('watchlists/',WatchListView.as_view(),name='watchlists'),
]

