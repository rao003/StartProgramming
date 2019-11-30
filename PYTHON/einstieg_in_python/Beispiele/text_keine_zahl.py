# Fehler abfangen
x = "15.3p"

try:
    x = float(x)
    print(x*2)
except:
    print("Zeichenkette kann nicht umgewandelt werden")

