from random import randint

class Pizza:
    """
    Базовый класс для пиццы.
    Характеристики рецепта пиццы:
    1) ингридиенты 
    2) название 
    3) logo
    Характеристика инстанса пиццы: 
    1) размер
    Методы:
    1) вывести словарь со всей информацией
    2) метод __eq__
    """
    name = ""
    ingredients = []
    logo = ""

    SIZEZ = ["L", "XL"]

    def __init__(self, size = "L"):
        """
        Создает инстанс пиццы и определяет единсвенную хар-ку -- размер
        """
        if size.upper() not in self.__class__.SIZEZ:
            raise ValueError(f"Please choose one of the following options: {self.__class__.SIZEZ}")
        self.size = size.upper()

    def dict(self) -> dict:
        """
        Возвращает все характеристики инстанса в виде словаря
        """
        return {
            "name": self.__class__.__name__,
            "logo": self.__class__.logo,
            "ingredients": self.__class__.ingredients,
            "size": self.size
        }

     

    def __eq__(self, other: object) -> bool:
        """
        Считаем что две пиццы одинаковы, 
        если они из одного класса и одного размера
        """
        return (
            type(self) == type(other)
            and (self.size, set(self.ingredients)) == (other.size, set(other.ingredients))
            # нужно ли проверять ингридиенты??
        )


class Margherita(Pizza):
    """
    Маргарита
    """
    ingredients = ["tomato sauce", "mozzarella", "tomatoes"]
    logo = "🧀"
    name = "Margherita"


class Pepperoni(Pizza):
    """
    Пепперони
    """

    ingredients = ["tomato sauce", "mozzarella", "pepperoni"]
    logo = "🍕"
    name = "Pepperoni"


class Hawaiian(Pizza):
    """гавайская пицца"""

    ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    logo = "🍍"
    name = "Hawaiian"




def log(foo):
    """
    Декоратор, который печатает название функции и случайное число
    Сама функция не вызывается
    """
    def wrapper(*args, **kwargs):
        random_time = randint(1, 10)
        print(f"{foo.__name__} -- {random_time} c")
    return wrapper

def apply_transform(text_str):
    """
    Параметризованный декоратор, который подставляет 
    случайное число в передаваемый шаблон.
    Сама функция не вызывается
    """
    def decorator(foo):
        def wrapper(*args, **kwargs):
            print(text_str.format(randint(1, 10)))
        return wrapper
    return decorator



@log
def bake(pizza: Pizza) -> None:
    """Готовит пиццу"""
    pass

@apply_transform("🧑‍🍳Приготовили за {}с!")
def beautiful_bake(pizza: Pizza) -> None:
    """Готовит пиццу"""
    pass

@apply_transform("🚚 Доставили за {}с!")
def beautiful_delivery(pizza: Pizza) -> None:
    """Доставляет пиццу"""
    pass

@apply_transform("🏠 Забрали за {}с!")
def beautiful_pickup(pizza: Pizza) -> None:
    """Осуществляет пиццу"""
    pass

if __name__ == '__main__':
    a = Hawaiian()
    b = Pepperoni("L")
    c = Pepperoni("XL")
    d = Margherita()
    print(a.logo, b.logo, c.logo, d.logo)
    print(a.dict())
    print(a == b)
    print(c == b)
    bake(a)
    beautiful_bake(b)
    beautiful_delivery()
    beautiful_pickup()