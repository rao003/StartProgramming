import tkinter

def ende():
    main.destroy()

def anzeigen():
    lb["text"] = "Auswahl: " + li.get("active")

main = tkinter.Tk()

# Listbox mit vier Elementen
li = tkinter.Listbox(main, height=0)
li.insert("end","Hamburg")
li.insert("end","Stuttgart")
li.insert("end","Berlin")
li.insert("end","Dortmund")
li.pack()

# Auswahl anzeigen lassen
bshow = tkinter.Button(main, text = "Anzeigen",
                       command = anzeigen)
bshow.pack()

# Anzeigelabel
lb = tkinter.Label(main, text = "Auswahl:")
lb.pack()

bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


