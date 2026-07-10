#!/usr/bin/python3
"""Export employee TODO list data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user = requests.get(user_url).json()
    username = user.get("username")

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    todos = requests.get(todos_url).json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)
