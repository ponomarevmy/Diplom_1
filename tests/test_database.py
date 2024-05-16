import pytest
from unittest import mock
from praktikum.database import Database


class TestDatabase:
    def test_available_buns_with_mocks(self):
        database = Database()
        mock_buns = [mock.Mock(name="black bun"), mock.Mock(name="white bun"), mock.Mock(name="red bun")]
        database.available_buns = mock.Mock(return_value=mock_buns)

        assert database.available_buns() == mock_buns

    def test_available_ingredients_with_mocks(self):
        database = Database()
        mock_ingredients = [mock.Mock(name="hot sauce"), mock.Mock(name="sour cream"), mock.Mock(name="chili sauce"),
                            mock.Mock(name="cutlet"), mock.Mock(name="dinosaur"), mock.Mock(name="sausage")]
        database.available_ingredients = mock.Mock(return_value=mock_ingredients)

        assert database.available_ingredients() == mock_ingredients

    @pytest.mark.parametrize("bun_name, bun_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_available_buns_parameterization(self, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()

        for bun in buns:
            if bun.name == bun_name:
                assert bun.price == bun_price

    @pytest.mark.parametrize("sous, ingredient_name, ingredient_price", [
        ("sauce", "hot sauce", 100),
        ("sauce", "sour cream", 200),
        ("sauce", "chili sauce", 300),
        ("filling", "cutlet", 100),
        ("filling", "dinosaur", 200),
        ("filling", "sausage", 300)
    ])
    def test_available_ingredients_parameterization(self, sous, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()

        for ingredient in ingredients:
            if ingredient.type == sous and ingredient.name == ingredient_name:
                assert ingredient.price == ingredient_price