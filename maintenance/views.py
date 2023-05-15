import csv

from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import NationalPokedex


class IndexView(TemplateView):
    template_name = "maintenance/export.html"


index = IndexView.as_view()


def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = 'attachment; filename="national_pokedex.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            "id",
            "name",
            "created_by",
            "created_at",
            "updated_by",
            "update_at",
            "is_deleted",
            "test_column",
        ]
    )

    national_pokedex = NationalPokedex.objects.all().values_list(
        "id",
        "name",
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "is_deleted",
    )
    for pokemon_data in national_pokedex:
        edited_pokemon_data = pokemon_data + ("test",)
        writer.writerow(edited_pokemon_data)

    return response
