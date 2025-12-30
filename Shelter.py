from Animal import Animal

class Shelter():
    def __init__(self):
        self.animals = {}
        self.adoptions = {}

    def add(self, animal: Animal) -> None:
        # se presente gia questo id viene sovrascitto animale
        self.animals[animal.id] = animal

    def get(self, animal_id: str) -> Animal | None:
        try:
            return self.animals[animal_id]
        except Exception:
            return None

    def list_all(self) -> list[Animal]:
        return [a for a in self.animals.values()]

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions

    def set_adopted(self, animal_id: str, adopter_name: str):
        self.adoptions[animal_id] = adopter_name




