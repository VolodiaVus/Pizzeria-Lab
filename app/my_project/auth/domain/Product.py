from typing import List


class Product:
    def __init__(self, idProducts: int, name: str, descr: str, price: float):
        self.id = idProducts
        self.name = name
        self.descr = descr
        self.price = price
        self.ingredients: List['Ingredient'] = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'descr': self.descr,
            'price': float(self.price),
            'ingredients': [ing.to_dict() for ing in self.ingredients]
        }