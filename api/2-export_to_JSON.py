#!/usr/bin/python3
"""Export an employee's TODO list data to JSON format."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
            "{}/users/{}".format(base_url, employee_id)) as response:
        user = json.loads(response.read().decode())

    with urllib.request.urlopen(
            "{}/todos?userId={}".format(base_url, employee_id)) as response:
        todos = json.loads(response.read().decode())

    username = user.get("username")
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username})

    data = {employee_id: tasks}
    filename = "{}.json".format(employee_id)

    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
