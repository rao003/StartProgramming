# Erzeugung
alter = {"Peter":31, "Julia":28, "Werner":35}
print(alter)

# Element enthalten?
if "Julia" in alter:
    print(alter["Julia"])

# Entfernen eines Elements
del alter["Julia"]

# Element enthalten?
if "Julia" not in alter:
    print("Julia ist nicht enthalten")

# Anzahl Elemente
print("Anzahl: ", len(alter))

# Aktualisierung mit zweitem Dictionary
ualter = {'Moritz': 18, 'Werner': 29}
alter.update(ualter)
print(alter)

