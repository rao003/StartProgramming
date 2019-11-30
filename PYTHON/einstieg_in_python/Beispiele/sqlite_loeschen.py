import sqlite3

def ausgabe():
    # SQL-Abfrage, senden, Ausgabe
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Vorher
ausgabe()

# Datensatz entfernen
sql = "DELETE FROM personen " \
      "WHERE personalnummer = 8339"
cursor.execute(sql)
connection.commit()

# Nachher
ausgabe()

connection.close()

