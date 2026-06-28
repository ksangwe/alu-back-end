#!/usr/bin/python3
"""Export all employees' TODO list data to a single JSON file."""
import json
import urllib.request


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen("{}/users".format(base_url)) as response:
        users = json.loads(response.read().decode())

    with urllib.request.urlopen("{}/todos".format(base_url)) as response:
        todos = json.loads(response.read().decode())

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[str(user_id)] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
