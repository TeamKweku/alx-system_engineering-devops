#!/usr/bin/python3
"""a script that returns information about a user TODO list"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    api_endpoint = "{}/users".format(url)
    users = requests.get(api_endpoint).json()

    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {
        user.get("id"): [
            {
                "username": user.get("username"),
                "tasks": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in tasks
            if task.get("userId") == user.get("id")
        ]
        for user in users
    }

    with open("todo_all_employees.json", "w") as file_obj:
        json.dump(user_tasks, file_obj)
