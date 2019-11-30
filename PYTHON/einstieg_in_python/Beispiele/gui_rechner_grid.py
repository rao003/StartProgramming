import sys, tkinter

def ende():
    main.destroy()

# Kehrwert
def kw():
    if not lb["text"]:
        return
    z = float(lb["text"])
    z = 1/z
    lb["text"] = str(z)

# Quadrat
def qu():
    if not lb["text"]:
        return
    z = float(lb["text"])
    z = z*z
    lb["text"] = str(z)

# Anzeige leeren
def cl():
    lb["text"] = ""

# Ziffern 0 bis 9
def anz(ziffer):
    lb["text"] += str(ziffer)

# Punkt, falls noch nicht vorhanden
def anzp():
    if lb["text"].find(".") == -1:
        lb["text"] += "."
    
main = tkinter.Tk()

# Row 0
lb = tkinter.Label(main, bg="#FFFFFF", bd=5,
                   relief="sunken", anchor="e")
lb.grid(row=0, column=0, columnspan=3, sticky="we")

# Row 1
tkinter.Button(main, text="1/x", width=7,
    command=kw).grid(row=1, column=0)
tkinter.Button(main, text="x hoch 2", width=7,
    command=qu).grid(row=1, column=1)
tkinter.Button(main, text="CL", width=7,
    command=cl).grid(row=1, column=2)

# Row 2
tkinter.Button(main, text="7", width=7, command=
    lambda:anz(7)).grid(row=2, column=0)
tkinter.Button(main, text="8", width=7, command=
    lambda:anz(8)).grid(row=2, column=1)
tkinter.Button(main, text="9", width=7, command=
    lambda:anz(9)).grid(row=2, column=2)

# Row 3
tkinter.Button(main, text="4", width=7, command=
    lambda:anz(4)).grid(row=3, column=0)
tkinter.Button(main, text="5", width=7, command=
    lambda:anz(5)).grid(row=3, column=1)
tkinter.Button(main, text="6", width=7, command=
    lambda:anz(6)).grid(row=3, column=2)

# Row 4
tkinter.Button(main, text="1", width=7, command=
    lambda:anz(1)).grid(row=4, column=0)
tkinter.Button(main, text="2", width=7, command=
    lambda:anz(2)).grid(row=4, column=1)
tkinter.Button(main, text="3", width=7, command=
    lambda:anz(3)).grid(row=4, column=2)

# Row 5
tkinter.Button(main, text=".", width=7,
    command=anzp).grid(row=5, column=0)
tkinter.Button(main, text="0", width=7,
    command=lambda:anz(0)).grid(row=5, column=1)
tkinter.Button(main, text="Ende", width=7,
    command=ende).grid(row=5, column=2)

main.mainloop()

