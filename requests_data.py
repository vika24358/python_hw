import requests
from pprint import pprint
from pywebio import start_server


url = 'https://dummyjson.com/todos?'

params = {
    'limit': 5,
    'skip': 0
}

# response = requests.get(url=url, params=params)
#
# # print(response)
# # print(response.content)
# # print(response.text)
# # pprint(response.json(), indent=4, width=80)
#
# response_json = response.json()
# todos = response_json['todos']
#
# completed_todos = 0
# for todo in todos:
#     if todo['completed']:
#         completed_todos += 1
#
# print(completed_todos)
#
#
# print()

def get_todos(limit: int = 50, start: int = 0) -> list[dict]:
    params = {
        'limit': limit,
        'skip': start
    }
    response = requests.get(url=url, params=params)
    response_json = response.json()
    todos = response_json['todos']
    return todos

def get_completed_todos_number(todos_candidates:list[dict], is_completed: bool = True) -> int:
    counter = 0
    for todo in todos_candidates:

        if todo['completed'] is is_completed:
            counter += 1
    return counter

def get_todos_by_content(todos_candidates:list[dict], content: str) -> list[str]:
    content_list = []
    for todo in todos_candidates:
        if content.lower() in todo['todo'].lower():
            content_list.append(todo['todo'])
    return content_list

def main():
    start = 0
    limit = 50

    completed_successfully = 0
    completed_unsuccessfully = 0
    content_lst = []
    content_word = 'solve'

    for iterator in range(1, 301):
        chunk = get_todos(start=start, limit=limit)
        if not chunk:
            break
        completed_successfully += get_completed_todos_number(chunk)
        completed_unsuccessfully += get_completed_todos_number(chunk, False)
        content_lst += get_todos_by_content(chunk, content_word)
        start += limit

    print(f'{completed_successfully=}, {completed_unsuccessfully=}')
    pprint(content_lst)

if __name__ == '__main__':
    start_server(main, port=15000)
