import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Eingabe Name
eingabe = input("Bitte den gesuchten Namen eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
cursor.execute(sql, (eingabe,))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Eingabe Teil des Namens
eingabe = input("Bitte den gesuchten Namensteil eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
eingabe = '%' + eingabe + '%'
cursor.execute(sql, (eingabe,))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

connection.close()

