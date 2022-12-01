#!/usr/bin/python3
"""Task 3: Write a Python script that, using this REST API,
for all tasks from all employees, returns information about
TODO list progress. Extended to export data a JSON file.
"""
import json
import requests
from sys import argv


def data_gather_all_to_json():
    """makes two get requests to the api
    """
    url1 = 'https://jsonplaceholder.typicode.com/todos/'
    url2 = 'https://jsonplaceholder.typicode.com/users/'
    todo_res = requests.get(url1)
    user_res = requests.get(url2)

    todo_res = todo_res.json()
    user_res = user_res.json()
    
    employeeDict = {}
    fullDict = {}

    for employee in user_res:
        employeeDict[employee.get('id')] = []
        fullDict[employee.get('id')] = employee.get('username')

    for task in todo_res:
        taskD = {}
        taskD['username'] = fullDict.get(task.get('userId'))
        taskD['task'] = task.get('title')
        taskD['completed'] = task.get('completed')
        employeeDict.get(task.get('userId')).append(taskD)

    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump(employeeDict, f)


if __name__ == "__main__":
    data_gather_all_to_json()
