import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Rye bun", 2.50)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize(
        'ingredient, expected_result', [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, ['SAUCE']),
            (ingredient_types.INGREDIENT_TYPE_FILLING, ['FILLING'])
        ]
    )
    def test_add_ingredient(self, ingredient, expected_result):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == expected_result

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Salad", "Cheese", 0.60)
        ingredient2 = Ingredient("Tomato", "Fillet", 0.85)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Salad", "Cheese", 0.60)
        ingredient2 = Ingredient("Tomato", "Fillet", 0.85)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Bun("Red bun", 1.50)
        ingredient1 = Ingredient("Salad", "Cheese", 0.60)
        ingredient2 = Ingredient("Tomato", "Fillet", 0.85)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 4.45

    def test_get_receipt(self):
        bun = Bun("Red bun", 1.50)
        ingredient1 = Ingredient("Salad", "Cheese", 0.60)
        ingredient2 = Ingredient("Tomato", "Fillet", 0.85)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        print(receipt)
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'= {ingredient1.get_type().lower()} {ingredient1.get_name()} =' in receipt
        assert f'= {ingredient2.get_type().lower()} {ingredient2.get_name()} =' in receipt
        assert f'Price: {burger.get_price()}' in receipt