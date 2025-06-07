import requests
from pytest_steps import test_steps

from modules.goals_methods import create_goal, get_goals, get_goal_by_id, update_goal, delete_goal
from faker import Faker
fake = Faker()


my_headers = {"Authorization": "pk_200462817_COO7ES7D50MAEEI9FB3Q3P5GSV4Z829G",
              "Content-Type": "application/json"}

def test_get_goals():
    result = get_goals()
    assert result.status_code == 200

def test_get_goals_without_token():
    header = {"Authorization": ""}
    result = requests.get("https://api.clickup.com/api/v2/team/90151225619/goal", headers=header)
    assert result.status_code == 400

@test_steps("Create goal", "Check created goal by id", "Delete created goal")
def test_create_goal():
    result = create_goal()
    assert result.status_code == 200
    yield

    goal_id = result.json()["goal"]["id"]
    result_get_goal = get_goal_by_id(goal_id)
    assert result_get_goal.status_code == 200
    assert result_get_goal.json()["goal"]["id"] == goal_id
    yield

    result_delete_goal = delete_goal(goal_id)
    assert result_delete_goal.status_code == 200
    yield


def test_create_goal_without_name():
    body = {}
    result = requests.post("https://api.clickup.com/api/v2/team/90151225619/goal", headers=my_headers, json=body)
    assert result.status_code == 500

@test_steps("Create goal", "Check created goal by id", "Delete created goal")
def test_get_goal_by_id():
    result = create_goal()
    assert result.status_code == 200
    yield

    goal_id = result.json()["goal"]["id"]
    result_get_goal = get_goal_by_id(goal_id)
    assert result_get_goal.status_code == 200
    assert result_get_goal.json()["goal"]["id"] == goal_id
    yield

    result_delete_goal = delete_goal(goal_id)
    assert result_delete_goal.status_code == 200
    yield

@test_steps("Create goal", "Get goal by invalid id", "Delete created goal")
def test_get_goal_by_invalid_id():
    result = create_goal()
    assert result.status_code == 200
    yield

    invalid_goal_id = "1111"
    result_get_goal = requests.get("https://api.clickup.com/api/v2/goal/" + invalid_goal_id, headers=my_headers)
    assert result_get_goal.status_code == 500
    yield

    goal_id = result.json()["goal"]["id"]
    result_delete_goal = delete_goal(goal_id)
    assert result_delete_goal.status_code == 200
    yield

@test_steps("Create goal", "Update goal by id", "Delete created and updated goal")
def test_update_goal():
    result = create_goal()
    assert result.status_code == 200
    yield

    goal_id = result.json()["goal"]["id"]
    result_update_goal = update_goal(goal_id)
    assert result_update_goal.status_code == 200
    yield

    result_delete_goal = delete_goal(goal_id)
    assert result_delete_goal.status_code == 200
    yield

@test_steps("Create goal", "Delete created goal")
def test_delete_goal():
    result = create_goal()
    assert result.status_code == 200
    yield

    goal_id = result.json()["goal"]["id"]
    result_delete_goal = delete_goal(goal_id)
    assert result_delete_goal.status_code == 200
    yield
