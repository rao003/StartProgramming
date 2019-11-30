import tkinter

def ende():
    main.destroy()

main = tkinter.Tk()

button = tkinter.Button(main, text="Ende",
                        command=ende)
button.pack()

# Erzeugen der Scrollbar
scb = tkinter.Scrollbar(main, orient="vertical")

# Erzeugen der Listbox, Verbindung mit der Scrollbar
li = tkinter.Listbox(main, height=4,
                     yscrollcommand=scb.set)
scb["command"] = li.yview

# Sieben Elemente
stadt = ["Hamburg", "Stuttgart", "Berlin", "Dortmund",
         "Duisburg", "Potsdam", "Halle"]
for s in stadt:
    li.insert("end", s)

# Anzeigen von Listbox und Scrollbar
li.pack(side="left")
scb.pack(side="left", fill="y")

main.mainloop()


