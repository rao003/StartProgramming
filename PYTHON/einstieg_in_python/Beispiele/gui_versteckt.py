import tkinter

def ende():
    main.destroy()

# Untersuchung des Passwortes
def pwtest():
    eingabe = e.get()
    if eingabe == "Bingo":
        lb["text"] = "Zugang erlaubt"
    else:
        lb["text"] = "Zugang verweigert"

main = tkinter.Tk()

# Eingabefeld mit Zeichen * als Darstellung
e = tkinter.Entry(main, show = "*")
e.pack()

# Test der Eingabe
btest = tkinter.Button(main, text = "Login",
                       command = pwtest)
btest.pack()

# Anzeige des Ergebnisses
lb = tkinter.Label(main, text = "Zugang")
lb.pack()

bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


