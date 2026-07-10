#!/usr/bin/python3
"""Export employee TODO list data to CSV format."""
import csv
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

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
