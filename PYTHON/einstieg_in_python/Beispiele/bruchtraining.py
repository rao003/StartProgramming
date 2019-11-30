import random
random.seed

# Tupel
prim = 2, 3, 5, 7
prob = 2, 2, 2, 2, 3, 3, 3, 5, 5, 7
ops = '+', '-', '*', '/'

# Funktion produkt()
def produkt(anzahl):
    wert = 1
    for i in range(anzahl):
        wert *= random.choice(prob)
    if random.randint(0,1) == 0:
        return wert
    else:
        return -wert

# Funktion kuerzen()
def kuerzen(ergz, ergn):
    for p in prim:
        while ergz%p == 0 and ergn%p == 0:
            ergz /= p
            ergn /= p
    if ergn < 0:
        ergz = -ergz
        ergn = -ergn
    return int(ergz), int(ergn)

# Funktion ergebnis()
def ergebnis(ergz, ergn):
    ergz, ergn = kuerzen(ergz, ergn)
    if ergn == 1:
        print("Ergebnis:", ergz)
    else:
        print("Ergebnis:", ergz, "/", ergn)
    
# Funktion leicht()
def leicht():
    ergw = random.randint(-10, 10)
    an = 0
    while an == 0:
        an = random.randint(-10, 10)
    az = ergw * an
    print("Ganze Zahl berechnen:", az, "/", an)
    input()
    print("Ergebnis:", ergw)

# Funktion mittel()
def mittel():
    ergz = produkt(3)
    ergn = produkt(3)
    print("Bruch kürzen:", ergz, "/", ergn)
    input()
    ergebnis(ergz, ergn)
    
# Funktion schwer()
def schwer():
    az = produkt(2)
    an = produkt(2)
    bz = produkt(2)
    bn = produkt(2)
    op = random.choice(ops)
    print("Ergebnis-Bruch berechnen: ", az, "/",
        an, " ", op, " ", bz, "/", bn, sep="")

    if op == '+':
        ergz = az * bn + an * bz
        ergn = an * bn
    elif op == '-':
        ergz = az * bn - an * bz
        ergn = an * bn
    elif op == '*':
        ergz = az * bz
        ergn = an * bn
    else:
        ergz = az * bn
        ergn = an * bz

    input()
    ergebnis(ergz, ergn)
    
# Hauptprogramm
while 1:
    # Eingabemenü 
    fehler = 1
    while fehler == 1:
        print()
        print("Ihre Wahl: 1=Leicht, 2=Mittel, 3=Schwer, 0=Ende")
        try:
            wahl = int(input())
            fehler = 0
            if wahl < 0 or wahl > 3:
                fehler = 1
                print("Bitte nur 0, 1, 2 oder 3 eingeben")
        except:
            print("Bitte nur 0, 1, 2 oder 3 eingeben")

    if wahl == 0:
        break
    elif wahl == 1:
        leicht()
    elif wahl == 2:
        mittel()
    else:
        schwer()

