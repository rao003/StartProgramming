import os
eintrag_iterator = os.scandir(".")

# Alle Dateien eines Verzeichnisses
for x in eintrag_iterator:
    # Nur falls gemäß schr*.py
    if x.name.startswith('schr') and x.name.endswith('.py'):
        # Zugriffsversuch
        try:
            d = open(x)
        except:
            print("Dateizugriff nicht erfolgreich")
            continue

        # Text einlesen
        gesamtertext = d.read()

        # Zugriff auf Datei beenden
        d.close()

        # Suchtext suchen
        if gesamtertext.find("obst") != -1:
            print(x.name)

# Schließt den Iterator
eintrag_iterator.close()

        
