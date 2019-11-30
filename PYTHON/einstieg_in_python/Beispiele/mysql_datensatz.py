# Connector importieren
import sys, mysql.connector

# Verbindung zur Datenbank auf dem Datenbankserver erstellen
connection = mysql.connector.connect(host = "localhost", \
    user = "root", passwd = "", db = "firma")

# Execution-Objekt erzeugen
cursor = connection.cursor()

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Maier', " \
    "'Hans', 6714, 3500, '1962-03-15')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Schmitz', " \
    "'Peter', 81343, 3750, '1958-04-12')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Mertens', " \
    "'Julia', 2297, 3621.5, '1959-12-30')"
cursor.execute(sql)
connection.commit()

# Execution-Objekt schliessen
cursor.close()

# Verbindung schliessen
connection.close()
