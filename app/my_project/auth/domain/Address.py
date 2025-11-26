

class Address:
    def __init__(self, idAddresses: int, idCustomers: int, street: str, city: str, house_number: str,
                 apartment: str = None):
        self.id = idAddresses
        self.customer_id = idCustomers
        self.street = street
        self.city = city
        self.house_number = house_number
        self.apartment = apartment

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'street': self.street,
            'city': self.city,
            'house_number': self.house_number,
            'apartment': self.apartment
        }