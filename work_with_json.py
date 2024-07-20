import json

data = {
    'name': 'Alex',
    'available': False,
    'age': 15,
    'hobbies': ['soccer', 'football']
}

to_string = json.dumps(data)

print(to_string)

from_string = json.loads(to_string, parse_int=float)
print(from_string)

with open('data.json', mode='w') as json_file:
    json.dump(data, json_file, indent=4)

with open('data.json', mode='r') as json_file2:
    data2 = json.load(json_file2)
    print(777777777)
    print(data2)
