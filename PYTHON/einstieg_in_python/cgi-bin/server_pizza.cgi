#!C:\Python38\python.exe

# Modul cgi
import cgi, cgitb

# Allgemeine Check-Funktion
def chk(element):
        global form
        if element in form:
                erg = form[element].value
        else:
                erg = ""
        return erg

# Ausgabe bei Fehler
cgitb.enable()

# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

print("Content-type: text/html")
print()
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")

# Anrede
print("<p>Guten Tag", chk("vn"), chk("nn"), "</p>")

# Adresse
print("<p>Ihre Adresse:", chk("st"), chk("hn"),
      "in", chk("pz"), chk("or"), "</p>")

# Pizza-Typ
print("<p>Ihre Bestellung: Pizza", chk("pt"))

# Beginn Berechnung Preis
preisliste = {"Salami":6, "Thunfisch":6.5,
                "Quattro Stagioni":7.5, "Python":8.5}
preis = preisliste[form["pt"].value]

# Zusatz
zusatzliste = {"Pepperoni":1, "Oliven":1.2,
                 "Sardellen":1.5}
if "zu" in form:
    try:
        print("mit", form["zu"].value)
        preis += zusatzliste[form["zu"].value]
    except:
        for element in form["zu"]:
                print(", mit", element.value)
                preis += zusatzliste[element.value]
print("</p>")

# Express-Service
if "ex" in form:
        print("<p>Mit Express-Service</p>")
        preis += 1.5

# Bemerkung
if "bm" in form:
        print("<p>Bemerkung:", form["bm"].value, "</p>")

# Rabatt
if "kc" in form:
        if form["ku"].value == "S" \
           and form["kc"].value == "Bingo":
                preis = preis * 0.95
                print("<p>Rabatt 5%</p>")

# Preis
print(f"Preis (ohne Bemerkung): {preis:.2f} &euro;")

print("</body>")
print("</html>")
