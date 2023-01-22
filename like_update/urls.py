from django.urls import path

from . import views

urlpatterns = [
    path("", views.like_dislike_view, name='home'),
    path("update_count/", views.update_count, name='update_count'),
]
