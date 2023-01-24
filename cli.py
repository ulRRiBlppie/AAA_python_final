import click
import pizza

list_of_recipes = pizza.Pizza.__subclasses__()



@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('recipe', nargs=1)
def order(recipe: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza.beautiful_bake()
    if delivery:
        pizza.beautiful_delivery()
    else:
        pizza.beautiful_pickup()
    print("Оцените пиццу от 1 до 5:")
    mark = int(input())
    print(f'Ваша оценка: {"⭐"*mark}, спасибо за заказ!')

@cli.command()
def menu():
    """Выводит меню"""
    for recipe in list_of_recipes:
        print('- ', recipe.name, recipe.logo, ':', ', '.join(recipe.ingredients))




if __name__ == '__main__':
    cli()

    order()
    menu()

