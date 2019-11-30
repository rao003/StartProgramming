# Originalliste
fr = ["Paris","Lyon","Marseille","Bordeaux"]
print("Original:")
print(fr)

# Ersetzen eines Elementes durch ein Element
fr[2] = "Lens"
print("Element ersetzt:")
print(fr)

# Ersetzen eines Teilbereiches durch eine Liste
fr[1:3] = ["Nancy","Metz","Gap"]
print("Teil ersetzt:")
print(fr)

# Entnehmen eines Teilbereiches
del fr[3:]
print("Teil entnommen:")
print(fr)

# Ersetzen eines Elementes durch eine Liste
fr[0] = ["Paris-Nord","Paris-Sud"]
print("Element durch Liste ersetzt:")
print(fr)



