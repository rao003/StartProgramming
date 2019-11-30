# Mehrere iterierbare Objekte
plz = [49808, 78224, 55411]
stadt = ["Lingen", "Singen", "Bingen"]
bundesland = ["NS", "BW", "RP"]

# Verbinden
kombi = zip(plz, stadt, bundesland)

# Ausgabe
for element in kombi:
    print(element)
