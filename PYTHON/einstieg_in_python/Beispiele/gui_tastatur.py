import tkinter

def ende():
    main.destroy()

def kev(e):
    lbanz["text"] = "Zeichen:" + e.char \
       + ", Beschreibung: " + e.keysym \
       + ", Codezahl: " + str(e.keycode)

main = tkinter.Tk()

# Key-Events
e = tkinter.Entry(main)
e.bind("<p>",kev)
e.bind("<+>",kev)
e.bind("<%>",kev)
e.bind("<,>",kev)
e.pack()

# Hilfe-Label
lbhlp = tkinter.Label(main,
        text = "Taste: p oder + oder % oder ,",
        width=40)
lbhlp.pack()

# Anzeigelabel
lbanz = tkinter.Label(main)
lbanz.pack()

# Schaltfläche Ende
bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


