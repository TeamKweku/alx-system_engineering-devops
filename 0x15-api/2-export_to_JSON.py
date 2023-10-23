#!/usr/bin/python3
"""a script that returns information about a user TODO list"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    user_id = int(sys.argv[1])
    api_endpoint = "{}/users/{}".format(url, user_id)
    username = requests.get(api_endpoint).json().get("username")

    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {
        user_id: [
            {
                "tasks": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in tasks
            if task.get("userId") == user_id
        ]
    }

    with open("{}.json".format(user_id), "w") as file_obj:
        json.dump(user_tasks, file_obj)
