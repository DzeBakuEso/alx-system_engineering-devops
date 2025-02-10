#!/usr/bin/python3
"""
Fetches TODO list data for a given employee ID and exports it to CSV.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Fetches and exports an employee's TODO list to a CSV file.

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

    user_id = user_data.get("id")
    username = user_data.get("username")

    file_name = f"{user_id}.csv"

    # Write data to CSV file
    with open(file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            csv_writer.writerow(
                [user_id, username, task["completed"], task["title"]]
            )


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("Usage: python3 1-export_to_CSV.py <employee_id>")

    export_to_csv(int(sys.argv[1]))
