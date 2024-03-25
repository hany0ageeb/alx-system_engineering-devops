#!/usr/bin/python3
"""Task 0. Gather data from an API
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
    1. You must use urllib or requests module
    2. The script must accept an integer as a parameter,
        which is the employee ID
    3. The script must display on the standard output the employee
        TODO list progress in this exact format:
        - First line: Employee EMPLOYEE_NAME is done
            with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            + EMPLOYEE_NAME: name of the employee
            + NUMBER_OF_DONE_TASKS: number of completed tasks
            + TOTAL_NUMBER_OF_TASKS: total number of tasks,
                which is the sum of completed and non-completed tasks
        - Second and N next lines display the title of completed tasks:
            TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
Example:
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
"""
import requests
import sys


def main():
    """Entry Point"""
    EMP_ID = sys.argv[1]
    r = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            EMP_ID))
    employee = r.json()
    r = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={'userId': EMP_ID})
    emp_tasks = r.json()
    completed_tasks = list(
        filter(
            lambda todo: todo.get("completed") is True,
            emp_tasks))
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'),
        len(completed_tasks),
        len(emp_tasks)))
    for task in completed_tasks:
        print('\t {}'.format(task.get("title")))


if __name__ == '__main__':
    main()
