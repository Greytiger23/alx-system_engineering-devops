#!/usr/bin/python3
"""script to export data in the JSON format"""


import requests
import json
from sys import argv


def get_todo(employee_id):
    """gets the todo list progress"""
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)
    a = requests.get(url)
    t = a.json()
    b = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
                     employee_id)).json().get("username")
    data = {employee_id: []}
    for todo in t:
        data[employee_id].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": b
        })
    x = "{}.json".format(employee_id)
    with open(x, mode='w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)
    try:
        employee_id = int(argv[1])
        get_todo(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)
