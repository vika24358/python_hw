import json

import requests

with open('new_book_file.pdf', mode='bw') as new_pdf_file:
    response = requests.get('https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf')
    new_pdf_file.write(response.content)


with open('json_homework.json', mode='w') as new_json_file:
    response2 = requests.get('http://api.open-notify.org/astros.json')
    json.dump(response2.json(), new_json_file, indent=4)
