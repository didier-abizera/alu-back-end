#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    todos = requests.get(todos_url).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
