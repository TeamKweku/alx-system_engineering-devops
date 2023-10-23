#!/usr/bin/python3
"""a script that returns information about a user TODO list"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    user_id = int(sys.argv[1])
    api_endpoint = "{}/users/{}".format(url, user_id)
    username = requests.get(api_endpoint).json().get("username")

    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = [
        [user_id, username, task.get("completed"), task.get("title")]
        for task in tasks
        if user_id == task.get("userId")
    ]

    with open("{}.csv".format(user_id), "w") as file_obj:
        writer = csv.writer(file_obj, quoting=csv.QUOTE_ALL, quotechar='"')

        for row in user_tasks:
            writer.writerow(row)
