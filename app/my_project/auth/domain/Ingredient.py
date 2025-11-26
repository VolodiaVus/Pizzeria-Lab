class Ingredient:
    def __init__(self, idIngredients: int, name: str):
        self.id = idIngredients
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }