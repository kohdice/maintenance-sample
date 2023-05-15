from django.urls import path

from . import views

app_name = "maintenance"
urlpatterns = [
    path("export/", views.index, name="export"),
    path("csv/", views.export_csv, name="csv"),
]
