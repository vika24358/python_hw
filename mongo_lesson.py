from pprint import pprint

import certifi
from pymongo.mongo_client import MongoClient

from config import USER_NAME, PASSWORD

uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster01.s4nondb.mongodb.net/?retryWrites=true&w=majority&appName=cluster01"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

db = client['books_db']

fantasy_books_coll = db['fantasy_books']
school_books_coll = db['school_books']

# fantasy_books_coll.insert_one({'title': 'Game of Thrones', 'price': 350, 'year_of_issue': 1996, 'number_of_pages': 865})

school_books_docs = [
    {'title': 'Історія України', 'grade': 10, 'amount_of_pages': 300},
    {'title': 'Англійська мова', 'grade': 11, 'amount_of_pages': 153},
    {'title': 'Математика', 'grade': 11, 'amount_of_pages': 415},
    {'title': 'Історія середніх віків', 'grade': 9, 'amount_of_pages': 237},
    {'title': 'Українська мова', 'grade': 10, 'amount_of_pages': 386},
]

# school_books_coll.insert_many(school_books_docs)

query = {
    'title': {'$regex': 'Історія*', '$options': 'i'}
}

result = school_books_coll.find(query)

pprint(list(result))
