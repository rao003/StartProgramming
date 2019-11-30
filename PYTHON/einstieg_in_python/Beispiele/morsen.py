import sys

# Erstellt Dictionary mit Morsezeichen aus Datei
def leseCode():
    # Lesen der Datei mit Zeichen und Morsezeichen
    try:
        d = open("morsen.txt")
    except:
        print("Dateifehler")
        sys.exit(0)
    allezeilen = d.readlines()
    d.close

    # Erste Zeichenkette in der Zeile ist das Zeichen
    # Es dient als Schlüssel für das Dictionary
    code = {}
    for zeile in allezeilen:
        worte = zeile.split()
        code[worte[0]] = worte[1]

    # Morsezeichen gleich, ob kleine oder große Buchstaben
    for i in range(97,123):
        code[chr(i)] = code[chr(i-32)]

    # Liste zurückliefern
    return code
