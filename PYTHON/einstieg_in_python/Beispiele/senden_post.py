import urllib.request, urllib.parse

# Eingabedaten
pnn = input("Bitte den Nachnamen eingeben: ")
pvn = input("Bitte den Vornamen eingeben: ")

# Dictionary mit Sendedaten, Codierung
dc = {b"nn":pnn, b"vn":pvn}
data = bytes(urllib.parse.urlencode(dc), "UTF-8")

# sendet Daten
u = urllib.request.urlopen \
   ("http://localhost/Python38/senden_post.php", data)

# Empfang der Antwort und Ausgabe
li = u.readlines()
u.close()
for element in li:
    print(element)
