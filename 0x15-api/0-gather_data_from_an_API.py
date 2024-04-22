#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""


import requests
from sys import argv


def get_todo(employee_id):
    """gets the todo list progress"""
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)
    a = requests.get(url)
    t = a.json()
    x = len(t)
    y = sum(1 for todo in t if todo.get('completed'))
    b = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
                     employee_id)).json().get("name")
    print("Employee {} is done with tasks({}/{}):".format(b, y, x))
    for todo in t:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))


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
