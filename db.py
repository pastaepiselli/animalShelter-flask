from Dog import Dog
from Cat import Cat
from Shelter import Shelter


milo = Dog("d1", "Milo", 5, 6.5, "Shizu", False)
nina = Cat("c1", "Nina", 4, 3.5, False, "Ball")
house = Shelter()

house.add(milo)
house.add(nina)

house.set_adopted("c1", "Lucrezia Le Foche")