#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
Requirements:
    1. Records all tasks that are owned by this employee
    2. Format must be:
        "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    3. File name must be: USER_ID.csv
"""
import csv
import requests
import sys


def main():
    """Entry point"""
    EMP_ID = sys.argv[1]
    r = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                EMP_ID))
    user_name = r.json().get('name')
    r = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': EMP_ID})
    tasks = r.json()
    with open(f"{EMP_ID}.csv", 'w') as f:
        writer = csv.writer(
                f,
                quotechar='"',
                quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                task.get('userId'),
                user_name,
                task.get('completed'),
                task.get('title')])


if __name__ == '__main__':
    main()
