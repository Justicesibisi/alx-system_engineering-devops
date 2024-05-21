#!/usr/bin/python3
"""
This module gathers data from an API and prints it.
"""

import json
import requests

def get_employee_tasks(employee_id):
    """
    Fetches tasks for a given employee id from the API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    user = response.json()
    
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todos = response.json()
    
    completed_tasks = [task for task in todos if task['completed']]
    
    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    get_employee_tasks(1)

