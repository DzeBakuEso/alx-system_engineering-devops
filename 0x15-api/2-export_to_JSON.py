#!/usr/bin/python3
"""Fetches TODO list data from an API and exports it to a JSON file."""

import json
import requests
import sys

if __name__ == "__main__":
    # Check if user ID is provided
    if len(sys.argv) < 2:
        sys.exit("Usage: ./2-export_to_JSON.py <USER_ID>")

    user_id = sys.argv[1]

    # Define API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    # Fetch user details
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Validate responses
    if user_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit("Error fetching data from API.")

    # Extract data
    user_data = user_response.json()
    todos_data = todos_response.json()
    username = user_data.get("username")

    # Format JSON data
    tasks_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    json_data = {str(user_id): tasks_list}

    # Write to JSON file
    filename = f"{user_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"Data exported to {filename}")
