# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin

from .models import NationalPokedex


class NationalPokedexResource(resources.ModelResource):
    class Meta:
        model = NationalPokedex


@admin.register(NationalPokedex)
class NationalPokedexAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "is_deleted",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"
    resource_class = NationalPokedexResource
