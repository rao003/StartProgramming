import sys

# Zugriffsversuch
try:
    d = open("schreiben.txt","w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Schreiben von einzelnen Strings, mit Zeilenende
d.write("Die erste Zeile\n")
for i in range(2,11,2):
    d.write(str(i) + " ")
d.write("\n")

# Schreiben einer Liste
x = ["abc\n", str(12/7.5)+"\n", "xyz\n"]
d.writelines(x)

# Schliessen der Datei
d.close()
