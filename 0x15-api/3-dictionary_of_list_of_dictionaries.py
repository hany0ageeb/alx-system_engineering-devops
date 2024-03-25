#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
Requirements:
    1. Records all tasks from all employees
    2. Format must be:
    {
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS},
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            }, ... ],
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS},
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS}, ... ]}
    3. File name must be: todo_all_employees.json
"""
import json
import requests


def main():
    """Entry Point"""
    all_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
    ).json()
    data = {}
    for user in all_users:
        tasks = list(map(
            lambda task: {
                'username': user.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed')
            },
            filter(
                lambda task: task.get('userId') == user.get('id'),
                all_tasks)))
        data[user.get('id')] = tasks
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
