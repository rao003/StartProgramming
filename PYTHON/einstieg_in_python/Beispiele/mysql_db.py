# Connector importieren
import sys, mysql.connector

# Verbindung zum Datenbankserver erstellen
try:
    connection = mysql.connector.connect \
        (host = "localhost", user = "root", passwd = "")
except:
    print("Keine Verbindung zum Server")
    sys.exit(0)

# Execution-Objekt erzeugen
cursor = connection.cursor()

# Datenbank erzeugen
cursor.execute("CREATE DATABASE IF NOT EXISTS firma")
connection.commit()

# Execution-Objekt schliessen
cursor.close()

# Verbindung schliessen
connection.close()
