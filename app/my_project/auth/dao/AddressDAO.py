from my_project.utils.mysql_connector import MySQLConnector
from typing import List, Dict


class AddressDAO:
    def __init__(self):
        self.connector = MySQLConnector()
    def get_by_customer_id(self, customer_id: int) -> List[Dict]:
        connection = self.connector.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    SELECT idAddresses, idCustomers, street, city, house_number, apartment 
                    FROM Addresses
                    WHERE idCustomers = %s;
                """
                cursor.execute(sql, (customer_id,))
                return cursor.fetchall()
        finally:
            connection.close()
