import requests
from faker import Faker
fake = Faker()
my_headers = {"Authorization": "pk_200462817_COO7ES7D50MAEEI9FB3Q3P5GSV4Z829G",
              "Content-Type": "application/json"}

def create_goal():
    body = {
        "name": fake.first_name()
    }
    return requests.post("https://api.clickup.com/api/v2/team/90151225619/goal", headers=my_headers, json=body)

def get_goals():
    return requests.get("https://api.clickup.com/api/v2/team/90151225619/goal", headers=my_headers)

def get_goal_by_id(goal_id):
    return requests.get("https://api.clickup.com/api/v2/goal/" + goal_id, headers=my_headers)

def update_goal(goal_id):
    body_new = {
        "name": fake.first_name()
    }
    return requests.put("https://api.clickup.com/api/v2/goal/" + goal_id, headers=my_headers, json=body_new)

def delete_goal(goal_id):
    return requests.delete("https://api.clickup.com/api/v2/goal/" + goal_id, headers=my_headers)
