import sys

# Zugriffsversuch
try:
    d = open("daten.csv","w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Schreiben einer Liste als CSV-Datensatz
li = [42, "Maier", 3524.52]
d.write(str(li[0]) + ";" + li[1] + ";"
    + str(li[2]).replace(".",",") + "\n")

# Schreiben einer zweidim. Liste als Datensatztabelle
dli = [[55, "Göçlü", 3185.00], [57, "Wäßmann", 2855.20]]
for element in dli:
    d.write(str(element[0]) + ";"
        + element[1] + ";"
        + str(element[2]).replace(".",",") + "\n")

# Schliessen der Datei
d.close()
