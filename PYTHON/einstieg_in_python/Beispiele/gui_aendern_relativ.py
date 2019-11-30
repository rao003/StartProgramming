import tkinter

def ende():
    main.destroy()

# Aktuelle Position
posx = 0
posy = 0

# bewegt nach links
def moveleft():
    global posx, posy
    posx -= 20
    lb.place(x=posx, y=posy, anchor="nw")

# bewegt nach rechts
def moveright():
    global posx, posy
    posx += 20
    lb.place(x=posx, y=posy, anchor="nw")

# bewegt nach oben
def moveup():
    global posx, posy
    posy -= 20
    lb.place(x=posx, y=posy, anchor="nw")

# bewegt nach unten
def movedown():
    global posx, posy
    posy += 20
    lb.place(x=posx, y=posy, anchor="nw")

# bewegt zur Startposition
def movestart():
    global posx, posy
    posx = 0
    posy = 0
    lb.place(x=posx, y=posy, anchor="nw")

main = tkinter.Tk()

# Frame mit bewegtem Label
fr1 = tkinter.Frame(main, width=200, height=150,
                    relief="sunken", bd=1)
fr1.pack(side="top")

# Frame mit Schaltflächen zur Bewegung
fr2 = tkinter.Frame(main, height=80)
fr2.pack(side="left")

# Frame mit Schaltfläche Ende
fr3 = tkinter.Frame(main, width=50, height=80)
fr3.pack(side="left")

# Bewegtes Label
lb = tkinter.Label(fr1, text="Test",
                   relief="sunken", bd=1)
lb.place(x=0, y=0, anchor="nw")

# bewegt nach links
bleft = tkinter.Button(fr2, text="nach links",
                       command=moveleft)
bleft.grid(row=1, column=0)

# bewegt nach rechts
bright = tkinter.Button(fr2, text="nach rechts",
                        command=moveright)
bright.grid(row=1, column=2)

# bewegt nach oben
bup = tkinter.Button(fr2, text="nach oben",
                     command=moveup)
bup.grid(row=0, column=1)

# bewegt nach unten
bdown = tkinter.Button(fr2, text="nach unten",
                       command=movedown)
bdown.grid(row=2, column=1)

# Startposition
bstart = tkinter.Button(fr2, text="Start",
                        command=movestart)
bstart.grid(row=1, column=1)

# Schaltfläche Ende
bende = tkinter.Button(fr3, text="Ende",
                       command=ende)
bende.place(relx=1, rely=1, anchor="se")

main.mainloop()

