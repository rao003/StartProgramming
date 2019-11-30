import tkinter

def ende():
    main.destroy()

def anzeigen():
    lb["text"] = "Zimmer " + du.get() + " " + mb.get()

main = tkinter.Tk()

# Anzeigelabel
lb = tkinter.Label(main, text = "Zimmer ", width=40)
lb.pack()

# Widget-Variablen
du = tkinter.StringVar()
du.set("ohne Dusche")
mb = tkinter.StringVar()
mb.set("ohne Minibar")

# Zwei Checkbuttons
cb1 = tkinter.Checkbutton(main, text="Dusche",
         variable=du, onvalue="mit Dusche",
         offvalue="ohne Dusche", command=anzeigen)
cb1.pack()
cb2 = tkinter.Checkbutton(main, text="Minibar",
         variable=mb, onvalue="mit Minibar",
         offvalue="ohne Minibar", command=anzeigen)
cb2.pack()

bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


