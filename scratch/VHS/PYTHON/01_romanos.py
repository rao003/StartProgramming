entry = int(input("digite seu numero"))

romano = ""
lista = ["I", "II", "III", "IV","V","VI","VII","VIII","IX"]


while(entry > 10):
    romano = romano + "X"
    entry = entry - 10

romano = romano + lista[entry-1]

print("seu numero", romano)
