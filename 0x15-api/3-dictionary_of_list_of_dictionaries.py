#!/usr/bin/python3
"""
Script that exports data in the JSON format.
"""

import json
import requests


def fetch_data():
    """
    Fetches user and task data from a REST API and exports it as a JSON file.
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        all_tasks[user_id] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos if task["userId"] == user_id
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    fetch_data()
