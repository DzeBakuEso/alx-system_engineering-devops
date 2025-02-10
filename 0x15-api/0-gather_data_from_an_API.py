#!/usr/bin/python3
"""
Fetches data from an API and displays TODO list progress
for a given employee ID.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user details
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if not user_data or not todos_data:
        return

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task["title"] for task in todos_data if task["completed"]]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(done_tasks)}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("Usage: python3 0-gather_data_from_an_API.py <employee_id>")

    get_employee_todo_progress(int(sys.argv[1]))
