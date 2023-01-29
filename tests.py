import pytest
import pizza
import re


@pytest.mark.parametrize(
    "some_pizza, expected_value",
    [
        (pizza.Margherita().dict(),
            {
                "ingredients": ["tomato sauce", "mozzarella", "tomatoes"],
                "logo": "🧀",
                "name": "Margherita",
                "size": "L"
            }
         ),
        (pizza.Margherita("XL").dict(),
            {
                "ingredients": ["tomato sauce", "mozzarella", "tomatoes"],
                "logo": "🧀",
                "name": "Margherita",
                "size": "XL"
            }
         ),
        (pizza.Pepperoni().dict(),
            {
                "ingredients": ["tomato sauce", "mozzarella", "pepperoni"],
                "logo": "🍕",
                "name": "Pepperoni",
                "size": "L"
            }
         ),
        (pizza.Hawaiian().dict(),
            {
                "ingredients": ["tomato sauce",
                                "mozzarella",
                                "chicken",
                                "pineapples"],
                "logo": "🍍",
                "name": "Hawaiian",
                "size": "L"
            }
         ),
    ],
)
def test_pizza(some_pizza, expected_value):
    """
    Тестирует, что у пицц правильные рецепты и
    характеристики: размер, логотип, название
    """
    assert dict(some_pizza) == expected_value


def test_bake(capfd):
    pizza.beautiful_bake(pizza.Pepperoni)
    out, _ = capfd.readouterr()
    print(out)
    assert (
        1 == 1
        and out[:18] == "🧑‍🍳Приготовили за "
        and 0 <= int(out[18]) <= 9
        and out[19:] == "с!\n"
    )


def test_beautiful_bake(capfd):
    pizza.beautiful_bake(pizza.Pepperoni)
    out, _ = capfd.readouterr()
    print(out)
    assert bool(re.match(r"🧑‍🍳Приготовили за ([0-9]|10)с!", out))


def test_beautiful_delivery(capfd):
    pizza.beautiful_delivery(pizza.Pepperoni)
    out, _ = capfd.readouterr()
    print(out)
    assert bool(re.match(r"🚚 Доставили за ([0-9]|10)с!", out))


def test_beautiful_pickup(capfd):
    pizza.beautiful_pickup(pizza.Pepperoni)
    out, = capfd.readouterr()
    print(out)
    assert bool(re.match(r"🏠 Забрали за ([0-9]|10)с!", out))
