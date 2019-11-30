import tkinter

def ende():
    main.destroy()

# Funktion zum Quadrieren und Ausgeben
def quad():
    eingabe = e.get()
    try:
        zahl = float(eingabe)
        lb["text"] = "Ergebnis: " + str(zahl * zahl)
    except:
        lb["text"] = "Bitte Zahl eingeben"

main = tkinter.Tk()

# einzeiliges Eingabefeld
e = tkinter.Entry(main)
e.pack()

# Schaltfläche zur Verarbeitung und Ausgabe
bquad = tkinter.Button(main,
           text = "Quadrieren", command = quad)
bquad.pack()

# Ausgabe-Label
lb = tkinter.Label(main, text = "Ergebnis:")
lb.pack()

bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


