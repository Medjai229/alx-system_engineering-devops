#!/usr/bin/python3
"""
This script is using JSONPlaceholder REST Api for a given employee ID
returns information about the user into a csv file
"""
from requests import get
from json import dump


if __name__ == "__main__":

    employees = get("https://jsonplaceholder.typicode.com/users")
    content = {}

    for employee in employees.json():
        USER_ID = str(employee.get("id"))
        employee_info = get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(USER_ID)).json()
        employee_todos = get("https://jsonplaceholder.typicode.com/todos",
                             params={"userId": USER_ID}).json()

        USERNAME = employee_info.get("username")

        file_info = []

        for task in employee_todos:
            TASK_COMPLETED_STATUS = task.get("completed")
            TASK_TITLE = task.get("title")

            task_info = {"username": USERNAME,
                         "task": TASK_TITLE,
                         "completed": TASK_COMPLETED_STATUS}
            file_info.append(task_info)

        content[USER_ID] = file_info

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        dump(content, file)
