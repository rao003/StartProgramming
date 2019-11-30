import sys
summe = 0

try:
    for i in sys.argv[1:]:
        summe += float(i)
    print("Ergebnis:", summe)
except:
    print("Parameterfehler")
