#!/usr/bin/python3
"""Gather data from an API for a given employee's TODO list progress."""
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

    name = user.get("name")
    done = [task for task in todos if task.get("completed")]
    total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), total))
    for task in done:
        print("\t {}".format(task.get("title")))
