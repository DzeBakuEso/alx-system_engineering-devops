#!/usr/bin/python3
"""
Script to fetch employee TODO list progress from an API
"""
import requests
import sys

def fetch_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information
    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print("Error: User not found")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Fetch user todos
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        fetch_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
