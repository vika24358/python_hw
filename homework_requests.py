import requests
from pywebio.output import put_html, put_text, put_table
from pywebio import start_server

# part 1
url1 = 'http://api.open-notify.org/astros.json'
url2 = 'https://dummyjson.com/users?limit=210'


def get_all_astronauts() -> list[dict]:
    response = requests.get(url=url1)
    response_json = response.json()
    names_astronauts = response_json['people']
    return names_astronauts


def get_astronauts_names(astronauts_candidates: list[dict]) -> list:
    astronauts_list = []
    for astronaut in astronauts_candidates:
        astronauts_list.append(astronaut['name'])
    return astronauts_list


def get_users() -> list[dict]:
    response = requests.get(url=url2)
    response_json = response.json()
    users = response_json['users']
    return users


def get_users_by_age(users_candidates: list[dict], required_age: int) -> list:
    table_data = [['First Name', 'Last Name']]
    for user in users_candidates:
        if user['age'] == required_age:
            table_data.append([user['firstName'], user['lastName']])
    return table_data


def main():
    # part 1
    astronauts_candidates = get_all_astronauts()
    astronauts_in_space = get_astronauts_names(astronauts_candidates)
    put_html('<h2>part1: The list of all astronauts in outer space</h2>')
    for name in astronauts_in_space:
        put_text(name)

    # part 2
    users_candidates = get_users()
    users_aged_twenty_eight = get_users_by_age(users_candidates, 28)
    put_html('<h2>part2: The list of all users aged 28</h2>')
    put_table(users_aged_twenty_eight)


if __name__ == '__main__':
    start_server(main, port=11000)
