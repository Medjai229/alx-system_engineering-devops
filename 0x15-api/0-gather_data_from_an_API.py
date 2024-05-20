#!/usr/bin/python3
""" API ToDo Module """
from requests import get
import sys


if __name__ == "__main__":
    num = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = get("{}users/{}".format(url, num)).json()
    todos = get("{}todos?userId={}".format(url, num)).json()
    tasks_done = [task for task in todos if task["completed"] is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user_data.get("name"), len(tasks_done), len(todos)))
    for task in tasks_done:
        print("\t {}".format(task.get("title")))
