import sqlite3
from pprint import pprint

DB_PATH = 'city_schools_db.sqlite3'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()
    query = """
        SELECT pupils_with_id.name, pupils_with_id.surname, city_schools.school_number, city_schools.address, city_schools.floor_number
        FROM pupils_with_id
        LEFT JOIN city_schools
        ON pupils_with_id.school_number = city_schools.school_number

    """
    result = cursor.execute(query)
    pprint(result.fetchall())

    # query = """
    #          ALTER TABLE pupils_with_id
    #          ADD COLUMN phone_number TEXT
    #     """
    # cursor.execute(query)

    query = """
        UPDATE pupils_with_id
        SET
        phone_number = '38099659418'
        WHERE id = 5
     """
    cursor.execute(query)

    query = """
         DELETE FROM pupils_with_id
         WHERE id BETWEEN 2 AND 6
     """
    cursor.execute(query)

    query = """
        SELECT name, surname
        FROM pupils_with_id
        
        ORDER BY id DESC
        LIMIT 3
    """
    result = cursor.execute(query)
    pprint(result.fetchall())
