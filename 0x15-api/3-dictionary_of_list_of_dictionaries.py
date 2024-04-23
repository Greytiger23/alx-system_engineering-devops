#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    a = requests.get(url)
    b = a.json()
    x = {}
    for user in b:
        user_id = str(user['id'])
        username = user['username']
        y = url + user_id + '/todos'
        c = requests.get(y)
        tasks = c.json()
        user_task = []
        for task in tasks:
            user_task.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
        x[user_id] = user_task
        with open('todo_all_employees.json', 'w') as json_file:
            json.dump(x, json_file)
