import requests as r
from sys import argv


def get_user_todos(employee_id):
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employee_id)
    resp_user = r.get(url_user)
    resp_todos = r.get(url_todos)
    try:
        users = resp_user.json()
        user_todos = resp_todos.json()
        completed_task = list(
            filter(lambda x: x.get("completed") is True,
                   user_todos))
        print("Employee {} is done with tasks({}/{}):"
              .format(users.get('name'), len(completed_task),
                      len(user_todos)))
        for todo in completed_task:
            print("\t {}".format(todo.get('title')))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    employee_id = argv[1]
    get_user_todos(employee_id)
