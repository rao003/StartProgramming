import tkinter, tkinter.messagebox

def ende():
    main.destroy()

def msginfo():
    tkinter.messagebox.showinfo \
       ("Info","Eine Info-Box")

def msgwarning():
    tkinter.messagebox.showwarning \
       ("Warnung","Eine Warnungs-Box")

def msgerror():
    tkinter.messagebox.showerror \
       ("Fehler","Eine Fehler-Box")

def msgyesno():
    antwort = tkinter.messagebox.askyesno \
       ("Ja/Nein", "Eine Ja/Nein-Box")
    if antwort == 1:
        lbanz["text"] = "Ja"
    else:
        lbanz["text"] = "Nein"

def msgokcancel():
    antwort = tkinter.messagebox.askokcancel \
       ("OK/Abbrechen", "Eine OK/Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "OK"
    else:
        lbanz["text"] = "Abbrechen"

def msgretrycancel():
    antwort = tkinter.messagebox.askretrycancel \
       ("Wiederholen/Abbrechen",
        "Eine Wiederholen/Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Abbrechen"

def msgfrage():
    # hier einmal in allgemeiner Technik, ohne Komfort
    msgbox = tkinter.messagebox.Message(main,
        type=tkinter.messagebox.ABORTRETRYIGNORE,
        icon=tkinter.messagebox.QUESTION,
        title="Beenden/Wiederholen/Ignorieren",
        message="Beenden, Wiederholen oder Ignorieren")
    
    antwort = msgbox.show()

    if antwort == "abort":
        lbanz["text"] = "Beenden"
    elif antwort == "retry":
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Ignorieren"

main = tkinter.Tk()

# Schaltfläche Message Info
binfo = tkinter.Button(main,
   text = "Info", command=msginfo)
binfo.pack()

# Schaltfläche Message Box Warning
bwarning = tkinter.Button(main,
   text = "Warnung", command=msgwarning)
bwarning.pack()

# Schaltfläche Message Box Error
berror = tkinter.Button(main,
   text = "Fehler", command=msgerror)
berror.pack()

# Schaltfläche Message Box Ja/Nein
byesno = tkinter.Button(main,
   text = "Ja/Nein", command=msgyesno)
byesno.pack()

# Schaltfläche Message Box OK/Cancel
bokcancel = tkinter.Button(main,
   text = "OK/Abbrechen", command=msgokcancel)
bokcancel.pack()

# Schaltfläche Message Box Retry/Cancel
bretrycancel = tkinter.Button(main,
   text = "Wiederholen/Abbrechen",
   command=msgretrycancel)
bretrycancel.pack()

# Schaltfläche Message Box Frage
bfrage = tkinter.Button(main,
   text = "Allgemeine Frage", command=msgfrage)
bfrage.pack()

# Schaltfläche Ende
bende = tkinter.Button(main,
   text = "Ende", command=ende)
bende.pack()

# Anzeige-Label
lbanz = tkinter.Label(main)
lbanz.pack()

main.mainloop()
