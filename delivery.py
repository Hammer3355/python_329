"""
Домашнее задание №23

Релизация классов для доставки товара, с учетом международной доставки и промо-кодов
Использование миксинов для расширения функционала классов а так же dataclass для хранения промо-кодов
"""


from dataclasses import dataclass
import json
from typing import List, Tuple, Union

class Product:
    """
    dimensions => габариты,
    weight => вес,
    fragility => хрупкость: True/False,
    price => хрупкость: цена,
    category => категория,
    name => название,
    """
    def __init__(self, dimentions: Tuple[float, float, float], weight: float, fragility: bool, price: float,
                 category: str, name: str):
        self.dimentions = dimentions
        self.weiht = weight
        self.fragility = fragility
        self.price = price
        self.category = category
        self.name = name


class Deliveri:
    def __init__(self, delivery_speed: int):
        self.delivery_speed = delivery_speed


    def calculate_cost(self,product: Product) -> float:
        return product.price * 0.01 + product.weiht * 0.05


@dataclass
class Promocode:
    """
    Датакласс хранит промокоды
    """
    code: str
    discount: int

    @classmethod
    def load_from_json(cls, filename: str) -> List["Promocode"]:
        with open("promocodes.json", "r") as file:
            data = json.load(file)
            return [cls(code=item["code"], discount=item["discount"]) for item in data]


# class InternationalMixin:
pr = Promocode
print(pr.load_from_json("promocodes.json"))