#!C:\Python38\python.exe

# Modul cgi
import cgi, cgitb

# Ausgabe bei Fehler
cgitb.enable()

# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

# Einzelne Elemente des Objekts
if "nn" in form:
    nn = form["nn"].value
if "vn" in form:
    vn = form["vn"].value

# HTML-Dokument mit Variablen
print("Content-type: text/html")
print()

print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")

print("<p><b>Registrierte Daten:</b></p>")
print("<p>Nachname:", nn, "</p>")
print("<p>Vorname:", vn, "</p>")

print("</body>")
print("</html>")
