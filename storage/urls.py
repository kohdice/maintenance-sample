from django.urls import path

from . import views

app_name = "storage"
urlpatterns = [
    path("loader/", views.index, name="loader"),
    path("upload/", views.upload_file, name="upload"),
]
