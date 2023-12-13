from django.contrib import admin
from django.urls import path

from backend import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("category/<str:name>/", views.category, name="category"),
    path("play_video/<int:video_id>/", views.play_video, name="play_video"),
    path("feed", views.feed, name="feed"),
    path("search/", views.search, name="search"),
    path("add_video_form/<str:name>/", views.add_video_form, name="add_video_form"),
    path("add_video_link/<str:name>/", views.add_video_link, name="add_video_link"),
    path("about/", views.about, name="about"),
]
