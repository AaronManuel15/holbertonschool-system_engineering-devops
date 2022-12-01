#!/usr/bin/python3
"""Task : Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress. Extended to export data in the CSV format.
"""
import csv
import requests
from sys import argv


def data_gather_to_csv():
    """makes two get requests to the api
    """
    url1 = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'
    todo_res = requests.get(url1.format(argv[1]))
    user_res = requests.get(url2.format(argv[1]))

    todo_res = todo_res.json()
    user_name = user_res.json().get("username")

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_res:
            line = [argv[1], user_name, task.get("completed"),
                    task.get("title")]
            writer.writerow(line)


if __name__ == "__main__":
    data_gather_to_csv()
