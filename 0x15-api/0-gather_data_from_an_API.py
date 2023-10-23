#!/usr/bin/python3
"""a script that returns information about a user TODO list"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    user_id = int(sys.argv[1])
    api_endpoint = "{}/users/{}".format(url, user_id)
    employee_name = requests.get(api_endpoint).json().get("name")

    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = [task for task in tasks if task.get("userId") == user_id]
    completed = [task for task in user_tasks if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed), len(user_tasks)
        )
    )

    for task in completed:
        print("\t {}".format(task.get("title")))
