import requests

url = 'https://script.google.com/macros/s/AKfycbzvDeEbQWzWRzF0wpWnIT8FG6o4fXsPJlaIMRAOFaX23q-P97p353JB_bdLo1dj5bcB/exec'


def get_animals() -> list[dict]:
    params = {'limit': 10}
    response = requests.get(url=url, params=params)
    response_json = response.json()
    animals = response_json['animals']
    return animals


def get_poisonous_animals_total_cost(animals: list[dict]) -> int | float:
    total_cost = 0
    for animal in animals:
        if animal['is_poisonous']:
            total_cost += animal['monthly_cost']
    return total_cost


def count_animals_from_africa(animals: list[dict]) -> int:
    animals_from_africa = 0
    for animal in animals:
        if animal['continent'] == "Африка":
            animals_from_africa += 1
    return animals_from_africa


def main():
    animals = get_animals()
    total_cost_poisonous_animals = get_poisonous_animals_total_cost(animals=animals)
    print(f'{total_cost_poisonous_animals=}')

    animals_from_africa = count_animals_from_africa(animals)
    print(f'{animals_from_africa=}')


if __name__ == "__main__":
    main()
