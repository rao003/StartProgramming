# Modul time
import time

# Zeit in Sekunden
print("Zeit in Sekunden:", time.time())

# Zeit in Nanosekunden
print("Zeit in Nanosekunden:", time.time_ns())

# Aktuelle, lokale Zeit als Tupel
lt = time.localtime()

# Entpacken des Tupels, Datum und Uhrzeit
jahr, monat, tag = lt[0:3]
stunde, minute, sekunde = lt[3:6]
print(f"Datum: {tag:02d}.{monat:02d}.{jahr:4d}")
print(f"Uhrzeit: {stunde:02d}:{minute:02d}:{sekunde:02d}")

# Wochentag
wtage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
         "Freitag", "Samstag", "Sonntag"]
wtagnr = lt[6]
print(wtage[wtagnr])

# Tag des Jahres
tag_des_jahres = lt[7]
print(f"Tag {tag_des_jahres:d} des Jahres")

# Sommerzeit
dst = lt[8]
if dst == 1:
    print("Die Sommerzeit ist aktiv")
elif dst == 0:
    print("Die Sommerzeit ist nicht aktiv")
else:
    print("Keine Sommerzeitinformation vorhanden")
