from my_project.utils.mysql_connector import MySQLConnector
from my_project.auth.domain.Product import Product
from my_project.auth.domain.Ingredient import Ingredient
from typing import List, Dict, Union


class ProductDAO:
    def __init__(self):
        self.connector = MySQLConnector()


    def get_by_id(self, product_id: int) -> Union[Product, None]:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT idProducts, name, descr, price FROM Products WHERE idProducts = %s;"
                cursor.execute(sql, (product_id,))
                result = cursor.fetchone()

                if result:
                    product = Product(**result)
                    return product
                return None
        finally:
            connection.close()

    def get_ingredients_by_product_id(self, product_id: int) -> List[Dict]:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    SELECT i.idIngredients, i.name 
                    FROM PizzaIngredients pi
                    JOIN Ingredients i ON pi.idIngredients = i.idIngredients
                    WHERE pi.idProducts = %s;
                """
                cursor.execute(sql, (product_id,))
                return cursor.fetchall()
        finally:
            connection.close()
