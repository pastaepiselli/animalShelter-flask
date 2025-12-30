from flask import Flask, jsonify, url_for, request
from db import  *

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "welcome to Animal Shelter API",
                    "links": {
                        "list_animals": url_for("list_animals"),
                        "get_animal": url_for("get_animal", animal_id="c1"),
                        "get_food": url_for("get_food", animal_id="c1"),
                        "get_adopted": url_for("get_adopted", animal_id="c1")
                    }}), 200


@app.route("/animals")
def list_animals():
    all_animals = {}
    for a in house.list_all():
        all_animals[a.id] = a.info()
    return jsonify(all_animals), 200

@app.route("/animals/<string:animal_id>")
def get_animal(animal_id: str):
    if animal_id in house.animals:
        return jsonify(house.animals[animal_id].info())
    else:
        return jsonify({"error": "animal not found"}), 404

@app.route("/animals/<string:animal_id>/food")
def get_food(animal_id: str):
    if animal_id in house.animals:
        return jsonify({"id": animal_id, "daily_food_grams": house.animals[animal_id].daily_food_grams()}), 200
    else:
        return jsonify({"error": "animal not found"}), 404

@app.route("/animals/<string:animal_id>/adoption")
def get_adopted(animal_id: str):
    if animal_id in house.adoptions:
        return jsonify({"id": animal_id, "adopted": True, "adopter_name": house.adoptions[animal_id]}), 200
    else:
        return jsonify({"id": animal_id, "adopted": False})

@app.route("/animals/add", methods=['POST'])
def add_animal():
    newAnimal = request.get_json()
    if "type" not in newAnimal:
        return jsonify({"error": "must specify the type"}), 400 # bad request
    elif newAnimal["type"] == "cat":
        try:
            # controllo ci siano tutte le chiavi
            id = newAnimal["id"]
            name = newAnimal["name"]
            age_years = newAnimal["age_years"]
            weight_kg = newAnimal["weight_kg"]
            indoor_only = newAnimal["indoor_only"]
            favorite_toy = newAnimal["favorite_toy"]

            house.add(Cat(id, name, age_years, weight_kg, indoor_only, favorite_toy))
            return jsonify({
                "message": "animal created",
                "id": id,
                "url": url_for("get_animal", animal_id=id)
            }), 200
        except KeyError:
            return jsonify({"errore": "some data missing"}), 400 # bad request
    elif newAnimal["type"] == "dog":
        try:
            # controllo ci siano tutte le chiavi
            id = newAnimal["id"]
            name = newAnimal["name"]
            age_years = newAnimal["age_years"]
            weight_kg = newAnimal["weight_kg"]
            breed = newAnimal["breed"]
            is_trained = newAnimal["is_trained"]

            house.add(Dog(id, name, age_years, weight_kg, breed, is_trained))
            return jsonify({
                "message": "animal created",
                "id": id,
                "url": url_for("get_animal", animal_id=id)
            }), 200 # non creo una nuova risorsa vado solo a dare una conferma
        except KeyError:
            return jsonify({"error": "some data missing"}), 400 # bad request

@app.route("/animals/<string:animal_id>/adopt", methods=['POST'])
def adopt(animal_id: str):
    if animal_id in house.animals:
        adopter = request.get_json()
        try:
            adopter_name = adopter["adopter_name"]
            house.set_adopted(animal_id, adopter_name)
            return jsonify({
                "id": animal_id,
                "adopter_name": adopter_name,
                "adopted": True
            }), 201
        except KeyError:
            return jsonify({"error": "bad json format"}), 400
    else:
        return jsonify({"error": "animal id not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)


