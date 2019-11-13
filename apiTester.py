import requests
import json

BASE_URL = "http://127.0.0.1:5000"
JSON_HEADER = {"Content-Type": "application/json"}

def create_user(name):
    data = json.dumps({"name": name})
    response = requests.post(BASE_URL + "/users", data=data, headers=JSON_HEADER)

    if response:
        new_id = response.json()["id"]
        return new_id
    
    return -1

def all_users():
    response = requests.get(BASE_URL + "/users")

    if response:
        users = response.json()
        return users
    
    return []

def edit_user(id, new_name):
    data = json.dumps({"name": new_name})
    requests.put(BASE_URL + "/users/" + str(id), data=data, headers=JSON_HEADER)

def delete_user(id):
    requests.delete(BASE_URL + "/users/" + str(id))

def test_users():
    print(f"creating users for alice, bob, and steve")
    alice_id = create_user("alice")
    bob_id = create_user("bob")
    steve_id = create_user("steve")
    
    for user in all_users():
        print(f"Looking up users, found {user['name']} with id {user['id']}")

    print(f"editting steve")
    edit_user(steve_id, "steve holt")

    print(f"deleting alice")
    delete_user(alice_id)

    current_users = all_users()
    for user in current_users:
        print(f"Looking up users, found {user['name']} with id {user['id']}")

    return current_users


def create_topic(name):
    data = json.dumps({"name": name})
    response = requests.post(BASE_URL + "/topics", data=data, headers=JSON_HEADER)

    if response:
        new_id = response.json()["id"]
        return new_id
    
    return -1

def all_topics():
    response = requests.get(BASE_URL + "/topics")

    if response:
        topics = response.json()
        return topics
    
    return []

def edit_topic(id, new_name):
    data = json.dumps({"name": new_name})
    requests.put(BASE_URL + "/topics/" + str(id), data=data, headers=JSON_HEADER)

def delete_topic(id):
    requests.delete(BASE_URL + "/topics/" + str(id))

def test_topics():
    print(f"creating topics for python, hot sauce, and weather")
    python_id = create_user("python")
    sauce_id = create_user("hot sauce")
    weather_id = create_user("weather")
    
    for topic in all_topics():
        print(f"Looking up topics, found {topic['name']} with id {topic['id']}")

    print(f"editting hot sauce to be more generic")
    edit_user(sauce_id, "sauce")

    print(f"deleting weather")
    delete_user(weather_id)

    current_topics = all_topics()
    for topic in current_topics:
        print(f"Looking up topics, found {topic['name']} with id {topic['id']}")

    return current_topics

if __name__ == "__main__":
    #make some data

    users = test_users()
    topics = test_topics()
    #posts = test_posts()


