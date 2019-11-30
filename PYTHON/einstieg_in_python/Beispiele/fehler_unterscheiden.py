# Wiederholte Eingabe
fehler = True
while fehler:
    try:
        zahl = float(input("Eine positive Zahl: "))
        if zahl == 0:
            raise RuntimeError("Zahl gleich 0")
        if zahl < 0:
            raise RuntimeError("Zahl zu klein")
        kw = 1.0 / zahl
        fehler = False
    except ValueError:
        print("Fehler: keine Zahl")
    except ZeroDivisionError:
        print("Fehler: Zahl 0 eingegeben")
    except RuntimeError as e:
        print("Fehler:", e)

# Ausgabe
print("Der Kehrwert von", zahl, "ist", kw)
