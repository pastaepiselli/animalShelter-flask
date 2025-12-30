from Animal import Animal

class Dog(Animal):
    def __init__(self, id: str, nome: str, age_years: int, weight_kg: float, breed: str, is_trained: bool):
        super().__init__(id, nome, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self):
        return "dog"

    def daily_food_grams(self):
        return 200 + self.age_years * 50

