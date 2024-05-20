#!/usr/bin/python3
"""
This script is using JSONPlaceholder REST Api for a given employee ID
returns information about the user into a csv file
"""
from requests import get
from sys import argv
from csv import writer, QUOTE_ALL


if __name__ == "__main__":

	employee_info = get("https://jsonplaceholder.typicode.com/users/{}"
				 .format(argv[1])).json()
	employee_todos = get("https://jsonplaceholder.typicode.com/todos",
					  params={"userId": argv[1]}).json()
	
	# "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
	USER_ID = str(employee_info.get("id"))
	USERNAME = employee_info.get("username")

	for task in employee_todos:
		TASK_COMPLETED_STATUS = task.get("completed")
		TASK_TITLE = task.get("title")

		format = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
		file_name = USER_ID + ".csv"

		with open(file_name, "a") as file:
			w = writer(file, quoting=QUOTE_ALL)
			w.writerow(format)