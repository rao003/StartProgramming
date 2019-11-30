import sys

try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = x + y
    print("Ergebnis:", z)
except:
    print("Parameterfehler")
