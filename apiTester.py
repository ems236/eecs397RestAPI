import requests
import json

BASE_URL = "http://127.0.0.1:5000"
JSON_HEADER = {"Content-Type": "application/json"}

def create_user(name):
    data = json.dumps({"name": name})
    response = requests.post(BASE_URL + "/users", data=data, headers=JSON_HEADER)

    if response:
        new_id = response.json()["id"]
        print(f"new user id is {new_id}")
        return new_id
    
    return -1

if __name__ == "__main__":
    #make some data
    first_user = json.dumps({"name": "steve"})
    second_user = json.dumps({"name": "alice"})
    third_user = json.dumps({"name": "jeffrey"})

    new_id = create_user("alice")