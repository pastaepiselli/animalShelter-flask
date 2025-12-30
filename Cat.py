from Animal import Animal

class Cat(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, indoor_only: bool, favorite_toy: str) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self) -> str:
        return "cat"

    def daily_food_grams(self) -> float:
        return 100 + self.age_years * 30

    