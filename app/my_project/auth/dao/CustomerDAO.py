from my_project.utils.mysql_connector import MySQLConnector
from my_project.auth.domain.Customer import Customer
from typing import List


class CustomerDAO:
    def __init__(self):
        self.connector = MySQLConnector()
    def get_all(self) -> List[Customer]:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT idCustomers, name, phone, email FROM Customers;"
                cursor.execute(sql)
                result = cursor.fetchall()
                return [Customer(**row) for row in result]
        finally:
            connection.close()

    def get_by_id(self, customer_id: int) -> Customer:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT idCustomers, name, phone, email FROM Customers WHERE idCustomers = %s;"
                cursor.execute(sql, (customer_id,))
                result = cursor.fetchone()
                if result:
                    return Customer(**result)
                return None
        finally:
            connection.close()

    def create(self, customer: Customer) -> Customer:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO Customers (name, phone, email) VALUES (%s, %s, %s);"
                cursor.execute(sql, (customer.name, customer.phone, customer.email))
                connection.commit()
                customer.id = connection.insert_id()
                return customer
        finally:
            connection.close()

    def update(self, customer_id: int, customer: Customer) -> Customer:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE Customers SET name = %s, phone = %s, email = %s WHERE idCustomers = %s;"
                cursor.execute(sql, (customer.name, customer.phone, customer.email, customer_id))
                connection.commit()
                if cursor.rowcount > 0:
                    customer.id = customer_id
                    return customer
                return None
        finally:
            connection.close()

    def delete(self, customer_id: int) -> bool:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM Customers WHERE idCustomers = %s;"
                cursor.execute(sql, (customer_id,))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()