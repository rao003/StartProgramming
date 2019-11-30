import tkinter

# Erzeugt neues Fenster mit Schaltfläche Ende
def fenster():
    global status, neu
    if status != "main":
        return
    status = "neu"
    neu = tkinter.Toplevel(main)
    tkinter.Button(neu, text="Ende Neu",
        command=endeneu).pack()

# Ende neues Fenster
def endeneu():
    global status
    neu.destroy()
    status = "main"

# Ende Hauptfenster
def ende():
    if status == "main":
        main.destroy()

# Hauptfenster
main = tkinter.Tk()
status = "main"
tkinter.Button(main, text="Neu", command=fenster).pack()
tkinter.Button(main, text="Ende", command=ende).pack()
main.mainloop()
