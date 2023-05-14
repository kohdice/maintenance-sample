import pytest

from ..admin import NationalPokedexResource


@pytest.mark.django_db(transaction=True)
class TestExport:
    def test_export(self) -> None:
        dataset = NationalPokedexResource().export()
        print(dataset)
