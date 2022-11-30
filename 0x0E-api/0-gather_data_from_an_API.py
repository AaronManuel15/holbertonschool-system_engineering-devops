#!/usr/bin/python3
"""Task 0: Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress.
"""
import requests
from sys import argv


def data_gather():
    """makes two get requests to the api
    """
    url1 = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'
    todo_res = requests.get(url1.format(argv[1]))
    user_res = requests.get(url2.format(argv[1]))

    todo_res = todo_res.json()
    user_name = user_res.json().get("name")
    todo_length = len(todo_res)

    todo_list = []

    for item in todo_res:
        if item.get('completed') is True:
            todo_list.append(item.get("title"))

    success_count = len(todo_list)

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, success_count, todo_length))
    for item in todo_list:
        print('\t {}'.format(item))


if __name__ == "__main__":
    data_gather()
