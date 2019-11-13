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

def lookup_user(id):
    response = requests.get(BASE_URL + "/users/" + str(id))

    if response:
        return response.json()
    
    return None

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

    new_steve = lookup_user(steve_id)
    print(f"looking up editted steve. Found {new_steve['name']} with id {new_steve['id']}")

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

def lookup_topic(id):
    response = requests.get(BASE_URL + "/topics/" + str(id))

    if response:
        return response.json()
    
    return None

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
    python_id = create_topic("python")
    sauce_id = create_topic("hot sauce")
    weather_id = create_topic("weather")
    
    for topic in all_topics():
        print(f"Looking up topics, found {topic['name']} with id {topic['id']}")

    print(f"editting hot sauce to be more generic")
    edit_topic(sauce_id, "sauce")

    new_sauce = lookup_topic(sauce_id)
    print(f"looking up editted hot sauce. Found {new_sauce['name']} with id {new_sauce['id']}") 

    print(f"deleting weather")
    delete_topic(weather_id)

    current_topics = all_topics()
    for topic in current_topics:
        print(f"Looking up topics, found {topic['name']} with id {topic['id']}")

    return current_topics


def lookup_post(id, topic_id):
    response = requests.get(f"{BASE_URL}/topics/{topic_id}/posts/{id}")

    if response:
        return response.json()
    
    return None

def create_post(title, description, user_id, topic_id):
    data = json.dumps({"title": title, "description": description, "user_id": user_id})
    response = requests.post(f"{BASE_URL}/topics/{topic_id}/posts", data=data, headers=JSON_HEADER)

    if response:
        new_id = response.json()["id"]
        return new_id
    
    return -1

def all_posts(topic_id):
    response = requests.get(f"{BASE_URL}/topics/{topic_id}/posts")

    if response:
        posts = response.json()
        return posts
    
    return []

def edit_post(id, topic_id, new_title, new_description, new_user):
    data = json.dumps({"title": new_title, "description": new_description, "user_id": new_user})
    requests.put(f"{BASE_URL}/topics/{topic_id}/posts/{id}", data=data, headers=JSON_HEADER)

def delete_post(id, topic_id):
    requests.delete(f"{BASE_URL}/topics/{topic_id}/posts/{id}")

def test_posts(topics, users):
    print(f"creating posts with existing users and topics")
    python_post_help = create_post("Help with python", "I'm writing a rest api and testing it is really lame. Any advice?", topics[0]["id"], users[0]["id"])
    python_post_changelog = create_post("python 4.20 changelog", "It's 2029 and some people are still using python 2", topics[0]["id"], users[1]["id"])
    sauce_post = create_post("I got lost in the sauce please help", "There's just too much sauce", topics[1]["id"], users[0]["id"])
    
    for topic in topics:
        for post in all_posts(topic["id"]):
            print(f"Looking up posts in topic {topic['name']}, found {post['title']} {post['description']} with id {post['id']}")

    print(f"editting python changelog")
    edit_post(python_post_changelog, topics[0]["id"], "python 3.9 changelog", "Nothing much new", users[0]["id"])

    new_changelog = lookup_post(python_post_changelog, topics[0]["id"])
    print(f"looking up editted changelong. Found {new_changelog['name']} with id {new_changelog['title']} {new_changelog['description']} with id {new_changelog['id']}")

    print(f"deleting help post")
    delete_post(python_post_help, topics[0]["id"])

    current_posts = {}
    for topic in topics:
        current_posts[topic["id"]] = all_posts(topic["id"])
        for post in current_posts[topic["id"]]:
            print(f"Looking up posts in topic {topic['name']}, found {post['title']} {post['description']} with id {post['id']}")

    return current_posts

if __name__ == "__main__":
    #make some data

    users = test_users()
    topics = test_topics()
    posts = test_posts(topics, users)
    #test_votes()


