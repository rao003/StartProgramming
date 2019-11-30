import sys, urllib.request

# Verbindung zu einem URL
try:
    u = urllib.request.urlopen \
        ("http://localhost/Python38/url_lesen.htm")
except:
    print("Fehler")
    sys.exit(0)

# Liest alle Zeilen in eine Liste
li = u.readlines()

# Schliesst die Verbindung
u.close()

# Ausgabe der Liste
for element in li:
    print(element)
