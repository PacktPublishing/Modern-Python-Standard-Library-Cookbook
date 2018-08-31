import sqlite3


with sqlite3.connect('/tmp/test.db') as db:
    try:
        db.execute('''CREATE TABLE people (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT,
            surname TEXT,
            language TEXT
        )''')
    except sqlite3.OperationalError:
        # Table already exists
        pass

    sql = 'INSERT INTO people (name, surname, language) VALUES (?, ?, ?)'
    db.execute(sql, ("Alessandro", "Molina", "Italian"))
    db.execute(sql, ("Mika", "Häkkinen", "Suomi"))
    db.execute(sql, ("Sebastian", "Vettel", "Deutsch"))

with sqlite3.connect('/tmp/test.db') as db:
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    for row in cursor.execute('SELECT * FROM people WHERE language != :language',
                              {'language': 'Italian'}):
        print(dict(row))
