import time, random, glob, sqlite3, \
    tkinter, tkinter.messagebox

def auswertung():
    if status != "main":
        return

    # Zeit berechnen
    endzeit = time.time()
    differenz = endzeit - startzeit
    
    # Auswertung
    richtig = 0
    for i in range(5):
        try:
            # Falsche Eingabe abfangen
            if int(enliste[i].get()) == ergliste[i]:
                richtig = richtig + 1
        except:
            pass

    # Kein Highscore
    if richtig < 5:
        tkinter.messagebox.showinfo("Kein Highscore",
            "Leider kein Highscore")
        main.destroy()
        return
    
    ##### Highscore speichern, ausgeben #####

    # Highscore-DB nicht vorhanden, erzeugen
    if not glob.glob("gui_highscore.db"):
        con = sqlite3.connect("gui_highscore.db")
        cursor = con.cursor()
        sql = "CREATE TABLE daten(name TEXT, zeit REAL)"
        cursor.execute(sql)
        con.close()

    # Datensatz in DB schreiben
    con = sqlite3.connect("gui_highscore.db")
    cursor = con.cursor()
    sql = "INSERT INTO daten VALUES('" \
        + lbname["text"] + "'," + str(differenz) + ")"
    cursor.execute(sql)
    con.commit()
    con.close()

    # Highscores sortiert laden
    con = sqlite3.connect("gui_highscore.db")
    cursor = con.cursor()
    sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
    cursor.execute(sql)

    # Ausgabe Highscore
    ausgabe = ""
    i = 1
    for dsatz in cursor:
        ausgabe += str(i) + ". " + dsatz[0] + " " \
            + str(round(dsatz[1],2)) + " sec.\n"
        i = i+1
    tkinter.messagebox.showinfo("Highscore", ausgabe)
    con.close()
    main.destroy()

def endeneu():
    global startzeit, status
    lbname["text"] = enname.get()
    startzeit = time.time()
    status = "main"
    neu.destroy()

# Hauptprogramm
main = tkinter.Tk()

# Titel
lbtitel = tkinter.Label(main, text="Kopfrechnen")
lbtitel.grid(row=0, column=0, columnspan=6)

# Name
lbname = tkinter.Label(main, text="Spielername")
lbname.grid(row=1, column=0, columnspan=6)

# Aufgaben
enliste = []     # Liste der Entries
ergliste = []    # Liste der richtigen Ergebnisse
for i in range(5):
    # Aufgabe mit Ergebnis
    a = random.randint(10,30)
    b = random.randint(10,30)
    ergliste.append(a + b)

    # Aufgabenstellung
    tkinter.Label(main, text=str(i+1)+"."). \
        grid(row=i+2, column=0)
    tkinter.Label(main, text=a).grid(row=i+2, column=1)
    tkinter.Label(main, text="+").grid(row=i+2, column=2)
    tkinter.Label(main, text=b).grid(row=i+2, column=3)
    tkinter.Label(main, text="=").grid(row=i+2, column=4)

    # Eingabefeld
    en = tkinter.Entry(main)
    en.grid(row=i+2, column=5)
    enliste.append(en)

# Ergebnis
b = tkinter.Button(main, text="Fertig", \
                   command=auswertung)
b.grid(row=7, column=0, columnspan=6)

# Fenster zur Namenseingabe
neu = tkinter.Toplevel(main)
tkinter.Label(neu, text="Ihr Name:").pack()
enname = tkinter.Entry(neu)
enname.pack()
tkinter.Button(neu, text="Start", command=endeneu).pack()
status="neu"

main.mainloop()
