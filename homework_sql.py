import sqlite3

DB_PATH = 'city_schools_db.sqlite3'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()
    query = """
            CREATE TABLE IF NOT EXISTS city_schools(
            school_number INTEGER NOT NULL,
            address TEXT NOT NULL,
            floor_number INTEGER CHECK (floor_number > 1)
        )
        """
    cursor.execute(query)
    query = """        
            CREATE TABLE IF NOT EXISTS pupils(
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                school_number INTEGER,
                FOREIGN KEY (school_number) REFERENCES city_schools(school_number)
        )
        """
    cursor.execute(query)

    values = (29, 'Kharkiv', 4)
    query = """
        INSERT INTO city_schools(school_number, address, floor_number)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, values)

    values = (
        (89, "Kharkiv", 5),
        (50, 'Kharkiv', 3),
    )
    query = """
            INSERT INTO city_schools(school_number, address, floor_number)
            VALUES (?, ?, ?)
        """
    cursor.executemany(query, values)

    values = (
        ("Вікторія", "Мірошніченко", 29),
        ("Тарас", "Шевченко", 29),
        ("Володимир", "Зеленський", 29),
        ("Леся", "Українка", 29),
        ("Вася", "Пупкін", 89),
        ("Кіра", "Іванова", 89),
        ("Петро", "Самойлов", 89),
        ("Ліза", "Дмитренко", 50),
        ("Маша", "Задорожня", 50),
        ("Дмитро", "Валентинов", 50),
    )
    query = """
            INSERT INTO pupils(name, surname, school_number)
            VALUES (?, ?, ?)
        """
    cursor.executemany(query, values)
