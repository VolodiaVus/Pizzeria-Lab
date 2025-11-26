from my_project.auth.dao.ProductDAO import ProductDAO
from my_project.auth.domain.Product import Product
from my_project.auth.domain.Ingredient import Ingredient
from typing import List, Union


class ProductService:
    def __init__(self):
        self.product_dao = ProductDAO()

    def find_pizza_with_ingredients(self, product_id: int) -> Union[Product, None]:
        product = self.product_dao.get_by_id(product_id)

        if product:
            ingredients_data = self.product_dao.get_ingredients_by_product_id(product_id)
            ingredients = [Ingredient(**data) for data in ingredients_data]
            product.ingredients = ingredients

            return product
        return None
