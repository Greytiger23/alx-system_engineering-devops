#!/usr/bin/python3
"""script to export data in the CSV format"""


import csv
import requests
from sys import argv


def get_todo(employee_id):
    """gets the todo list progress"""
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)
    a = requests.get(url)
    t = a.json()
    b = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
                     employee_id)).json().get("username")
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in t:
            writer.writerow([
                employee_id,
                b,
                todo.get('completed'),
                todo.get('title')
            ])


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
