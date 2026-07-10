#!/usr/bin/python3
"""Export all employees TODO list data to JSON format."""
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        tasks = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
