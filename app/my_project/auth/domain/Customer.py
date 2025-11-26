from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from my_project.auth.domain.Address import Address


class Customer:
    def __init__(self, idCustomers: int, name: str, phone: str, email: str):
        self.id = idCustomers
        self.name = name
        self.phone = phone
        self.email = email
        self.addresses: List['Address'] = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'addresses': [a.to_dict() for a in self.addresses]
        }