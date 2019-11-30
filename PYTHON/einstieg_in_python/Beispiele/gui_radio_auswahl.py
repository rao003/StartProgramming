import tkinter

def ende():
    main.destroy()

def anzeigen():
    lb["text"] = "Auswahl: " + farbe.get()

main = tkinter.Tk()

# Widget-Variable
farbe = tkinter.StringVar()
farbe.set("rot")

# Gruppe von Radio-Buttons
rb1 = tkinter.Radiobutton(main, text="rot",
                          variable=farbe, value="rot")
rb1.pack()
rb2 = tkinter.Radiobutton(main, text="gelb",
                          variable=farbe, value="gelb")
rb2.pack()
rb3 = tkinter.Radiobutton(main, text="blau",
                          variable=farbe, value="blau")
rb3.pack()

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


