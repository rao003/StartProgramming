# Erste Funktion
def eingabe():
    global x
    x = input("Zahl: ")
    x = float(x)

# Zweite Funktion
def ausgabe():
    print(x*2)
    
# Hauptprogramm
eingabe()
ausgabe()
