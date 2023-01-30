import click
import pizza

list_of_recipes = pizza.Pizza.__subclasses__()


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--size", default="L")
@click.argument("recipe", nargs=1)
def order(recipe: str,  delivery: bool, size: str) -> None:
    """Готовит и доставляет пиццу"""
    if recipe.upper() not in [recipe.name.upper()
                              for recipe in list_of_recipes]:
        raise ValueError("Такой пиццы нет в нашем меню")

    if size.upper() not in pizza.Pizza.SIZEZ:
        raise ValueError(f"Мы готовим пиццы размера {pizza.Pizza.SIZEZ}")

    def find_recipe_by_name(pizza_name: str) -> pizza.Pizza:
        """
        Находит нужный рецепт по имени и возвращает класс
        """
        for recipe in list_of_recipes:
            if pizza_name.upper() == recipe.__name__.upper():
                return recipe
    ordered_pizza = find_recipe_by_name(recipe)(size)
    pizza.beautiful_bake(ordered_pizza)
    if delivery:
        pizza.beautiful_delivery(ordered_pizza)
    else:
        pizza.beautiful_pickup(ordered_pizza)
    print("Оцените пиццу от 1 до 5:")
    mark = int(input())
    print(f"Ваша оценка: {'⭐'*mark}, спасибо за заказ!")


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for recipe in list_of_recipes:
        print("- ", recipe.name, recipe.logo,
              ":", ", ".join(recipe.ingredients))


if __name__ == "__main__":
    cli()
