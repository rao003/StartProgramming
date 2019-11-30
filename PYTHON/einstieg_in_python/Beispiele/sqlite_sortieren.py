import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Sortierung absteigend
sql = "SELECT * FROM personen ORDER BY gehalt DESC"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[3])
print()

# Sortierung nach mehreren Feldern
sql = "SELECT * FROM personen ORDER BY name, vorname"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()

