# Funktion
def summe(*summanden):
    print(len(summanden), "Zahlen")
    print(summanden)
    erg = 0
    for s in summanden:
        erg += s
    print("Summe:", erg)

# Aufrufe
summe(3, 4)
summe(3, 8, 12, -5)
