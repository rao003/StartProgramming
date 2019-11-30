import tkinter

# Funktion zu Schaltfläche Ende
def ende():
    main.destroy()

# Hauptfenster
main = tkinter.Tk()

# Schaltfläche Ende
b = tkinter.Button(main, text = "Ende", command = ende)
b.pack()

# Endlosschleife
main.mainloop()
