# Originallste
fr = ["Paris","Lyon","Marseille"]
print("Original:")
print(fr)

# Einsetzen eines Elements
fr.insert(0,"Nantes")
print("Nach Einsetzen:")
print(fr)

# Sortieren der Elemente
fr.sort()
print("Nach Sortieren:")
print(fr)

# Umdrehen der Liste
fr.reverse()
print("Nach Umdrehen:")
print(fr)

# Entfernen eines Elements
fr.remove("Nantes")
print("Nach Entfernen:")
print(fr)

# Ein Element am Ende hinzu
fr.append("Paris")
print("Ein Element hinzu:")
print(fr)

# Anzahl bestimmter Elemente
print("Anzahl Elemente Paris:", fr.count("Paris"))

# Suchen bestimmter Elemente
print("Erste Position Paris:", fr.index("Paris"))



