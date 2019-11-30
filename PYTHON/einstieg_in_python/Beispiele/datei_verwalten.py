import sys, shutil, os, glob
print(glob.glob("le*.txt"))

# Existenz feststellen
if not os.path.exists("lesen.txt"):
    print("Datei nicht vorhanden")
    sys.exit(0)

# Datei kopieren
shutil.copy("lesen.txt","lesen_kopie.txt")
print(glob.glob("le*.txt"))

# Datei umbenennen
try:
    shutil.move("lesen_kopie.txt","lesen_neu.txt")
except:
    print("Fehler beim Umbenennen")
print(glob.glob("le*.txt"))

# Datei entfernen
try:
    os.remove("lesen_neu.txt")
except:
    print("Fehler beim Entfernen")
print(glob.glob("le*.txt"))
