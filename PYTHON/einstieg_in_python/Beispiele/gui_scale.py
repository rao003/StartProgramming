import tkinter

def ende():
    main.destroy()

def anzeigen(self):
    lb["text"] = "Geschwindigkeit: " \
        + str(scvwert.get()) + " km/h"

main = tkinter.Tk()

# Anzeigelabel
lb = tkinter.Label(main,
        text = "Geschwindigkeit: 0 km/h", width=25)
lb.pack()

# Widget-Variablen
scvwert = tkinter.IntVar()
scvwert.set(0)

# Scale Widget
scv = tkinter.Scale(main, width=20, length=200,
         orient="vertical", from_=0, to=200,
         resolution=5, tickinterval=20, label="km/h",
         command=anzeigen, variable=scvwert)
scv.pack()

bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


