from my_project.auth.dao.CustomerDAO import CustomerDAO
from my_project.auth.domain.Customer import Customer
from typing import List, Union


from my_project.auth.dao.AddressDAO import AddressDAO
from my_project.auth.domain.Address import Address


class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()
        self.address_dao = AddressDAO()

    def find_all(self) -> List[Customer]:
        return self.customer_dao.get_all()

    def find_by_id(self, customer_id: int) -> Union[Customer, None]:
        return self.customer_dao.get_by_id(customer_id)

    def find_by_id_with_addresses(self, customer_id: int) -> Union[Customer, None]:
        customer = self.customer_dao.get_by_id(customer_id)

        if customer:
            addresses_data = self.address_dao.get_by_customer_id(customer_id)
            addresses = [Address(**data) for data in addresses_data]
            customer.addresses = addresses

            return customer
        return None

    def create(self, customer: Customer) -> Customer:
        if not customer.phone or len(customer.phone) < 5:
            raise ValueError("Phone number is too short.")
        return self.customer_dao.create(customer)

    def update(self, customer_id: int, customer: Customer) -> Customer:
        return self.customer_dao.update(customer_id, customer)

    def delete(self, customer_id: int) -> bool:
        return self.customer_dao.delete(customer_id)