import tkinter

# Funktion zu den Schaltflächen
def ende():
    main.destroy()

# Hauptfenster
main = tkinter.Tk()

# Schaltfläche Ende 1
b1 = tkinter.Button(main, text = "Ende", command = ende)

# Schaltfläche Ende 2
b2 = tkinter.Button(main)
b2["text"] = "Auch Ende"
b2["command"] = ende

# Schaltfläche Ende 3
b3 = tkinter.Button(main)
b3.configure(text = "Ebenfalls Ende", command = ende)

# Schaltflächen 1 bis 3 anzeigen
b1.pack()
b2.pack()
b3.pack()

# Schaltflächen Ende 4 und Ende 5
b4 = tkinter.Button(main,text="4",command=ende).pack()
tkinter.Button(main,text="5",command=ende).pack()

# Endlosschleife
main.mainloop()


