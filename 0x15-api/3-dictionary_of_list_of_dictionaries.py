import json
import requests


def fetch_todo_all_employees():
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        user_tasks = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos if task["userId"] == user_id
        ]

        all_tasks[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    fetch_todo_all_employees()
