#!/usr/bin/python3
"""
This script is using JSONPlaceholder REST Api for a given employee ID
returns information about the user into a csv file
"""
from requests import get
from sys import argv
from json import dump


if __name__ == "__main__":

    employee_info = get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    employee_todos = get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": argv[1]}).json()

    USER_ID = str(employee_info.get("id"))
    USERNAME = employee_info.get("username")

    file_info = []

    for task in employee_todos:
        TASK_COMPLETED_STATUS = task.get("completed")
        TASK_TITLE = task.get("title")

        task_info = {"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS,
                     "username": USERNAME}
        file_info.append(task_info)

    content = {USER_ID: file_info}
    file_name = USER_ID + ".json"

    with open(file_name, "w", encoding="utf-8") as file:
        dump(content, file)
