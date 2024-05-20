#!/usr/bin/python3
"""
This script is using JSONPlaceholder REST Api for a given employee ID
returns information about his/her TODO list progress
"""
from requests import get
from sys import argv


if __name__ == "__main__":

    employee_info = get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    employee_todos = get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": argv[1]}).json()

    completed_tasks = []
    for task in employee_todos:
        if task["completed"]:
            completed_tasks.append(task)

    EMPLOYEE_NAME = employee_info.get("name")
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(employee_todos)

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
