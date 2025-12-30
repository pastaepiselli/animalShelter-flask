from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float) -> None:
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species(self):
        pass

    @abstractmethod
    def daily_food_grams(self):
        pass

    def info(self) -> dict:
        return (self.__dict__)

    def bmi_like(self) -> float:
        return self.weight_kg / (self.age_years + 1)

    

