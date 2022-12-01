#!/usr/bin/python3
"""Task 2: Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress. Extended to export data a JSON file.
"""
import json
import requests
from sys import argv


def data_gather_to_json():
    """makes two get requests to the api
    """
    url1 = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'
    todo_res = requests.get(url1.format(argv[1]))
    user_res = requests.get(url2.format(argv[1]))

    todo_res = todo_res.json()
    user_name = user_res.json().get("username")

    tasks = []
    for task in todo_res:
        taskD = {}
        taskD['task'] = task.get('title')
        taskD['completed'] = task.get('completed')
        taskD['username'] = user_name
        tasks.append(taskD)

    jsDict = {argv[1]: tasks}
    with open('{}.json'.format(argv[1]), 'w', encoding='UTF8') as f:
        json.dump(jsDict, f)


if __name__ == "__main__":
    data_gather_to_json()
