import json
import requests

def show_response(req) -> None:
    print("Status code: ", req.status_code)
    print(json.dumps(req.json(), indent=4))

def get_request(url):
    request = requests.get(url=url, headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    return request

def post_request(url, json):
    request = requests.post(url=url, json=json)
    return request

# index
print('Test index')
show_response(get_request("http://127.0.0.1:5000/"))

# get all animals
print("Test get all animals")
show_response(get_request("http://127.0.0.1:5000/animals"))

# get single animal (existent)
print("Test get animal (existent)")
show_response(get_request("http://127.0.0.1:5000/animals/c1"))

# get single animal (not existent)
print("Test get animal (not existent)")
show_response(get_request("http://127.0.0.1:5000/animals/c2"))

# get animal food (existent animal)
print("Test get animal food (existent animal)")
show_response(get_request("http://127.0.0.1:5000/animals/c1/food"))

# get animal food (not existent animal)
print("Test get animal food (not existent animal)")
show_response(get_request("http://127.0.0.1:5000/animals/c2/food"))

# get adopted animal
print("Test adoption (adopted)")
show_response(get_request("http://127.0.0.1:5000/animals/c1/adoption"))

# get adopted animal not adopted
print("Test adoption (not adopted)")
show_response(get_request("http://127.0.0.1:5000/animals/d1/adoption"))

# ORA SI PASSA ALLE POST

print("Test POST")

request = requests.post(url="http://127.0.0.1:5000/animals/add",
    json={
        "type": "cat",
        "id": "c5",
        "name": "Micia",
        "age_years": 3,
        "weight_kg": 4.2,
        "indoor_only": True,
        "favorite_toy": "ball"
    }
)

print("Status code:", request.status_code)
print(request.json())

show_response(post_request(url="http://127.0.0.1:5000/animals/add", json=
    {
        "type": "dog",
        "id": "d3",
        "name": "Rex",
        "age_years": 2,
        "weight_kg": 18.5,
        "breed": "border collie",
        "is_trained": True
    }
))

show_response(post_request(url="http://127.0.0.1:5000/animals/d1/adopt", json={
    "adopter_name": "Alessandro Popa"
}))



