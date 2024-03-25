#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
Requirements:
    1. Records all tasks that are owned by this employee
    2. Format must be:
{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    3. File name must be: USER_ID.json
"""
import json
import requests
import sys


def main():
    """Entry point"""
    USER_ID = sys.argv[1]
    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
    )
    username = r.json().get('username')
    r = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={'userId': USER_ID})
    tasks = list(map(
        lambda task: {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username},
        r.json()))
    with open(f'{USER_ID}.json', 'w') as f:
        json.dump({USER_ID: tasks}, f)


if __name__ == '__main__':
    main()
