import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient("SAUCE", "Cheese", 0.60)
        assert ingredient.get_price() == 0.60

    def test_get_name(self):
        ingredient = Ingredient("SAUCE", "Cheese", 0.60)
        assert ingredient.get_name() == "Cheese"

    def test_get_type(self):
        ingredient = Ingredient("SAUCE", "Cheese", 0.60)
        assert ingredient.get_type() == "SAUCE"
