import tkinter

def ende():
    main.destroy()

def mlinks(e):
    lbanz["text"] = "Linke Maus-Taste"

def mrechts(e):
    lbanz["text"] = "Rechte Maus-Taste"

def mstrglinks(e):
    lbanz["text"] = "Strg-Taste und linke Maus-Taste"

def maltlinks(e):
    lbanz["text"] = "Alt-Taste und linke Maus-Taste"

def mshiftlinks(e):
    lbanz["text"] = "Shift-Taste und linke Maus-Taste"

def mlinkslos(e):
    lbanz["text"] = "Linke Maus-Taste losgelassen"

def mbetreten(e):
    lbanz["text"] = "Schaltfläche betreten"

def mverlassen(e):
    lbanz["text"] = "Schaltfläche verlassen"

def mbewegt(e):
    lbanz["text"] = \
    "Koordinaten: x=" + str(e.x) + ", y=" + str(e.y)

main = tkinter.Tk()

# Label mit Events
im = tkinter.PhotoImage(file="rheinwerk.png")
lbm = tkinter.Label(main, image=im)
lbm.bind("<Button 1>", mlinks)
lbm.bind("<Button 3>", mrechts)
lbm.bind("<Control-Button 1>", mstrglinks)
lbm.bind("<Alt-Button 1>", maltlinks)
lbm.bind("<Shift-Button 1>", mshiftlinks)
lbm.bind("<ButtonRelease 1>", mlinkslos)
lbm.bind("<Motion>", mbewegt)
lbm.pack()

# Anzeigelabel
lbanz = tkinter.Label(main, width=35)
lbanz.pack()

# Schaltfläche Ende, mit Events
bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.bind("<Enter>", mbetreten)
bende.bind("<Leave>", mverlassen)
bende.pack()

main.mainloop()


