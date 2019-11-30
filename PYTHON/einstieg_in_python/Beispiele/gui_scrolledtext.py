import tkinter, tkinter.scrolledtext

def ende():
    main.destroy()

# Anzeigefunktion
def xshow():
    d = open("gui_text.txt")
    z = d.readline()
    while z:
        t.insert("end",z)
        z = d.readline()
    d.close()
    
main = tkinter.Tk()

# mehrzeiliges Eingabefeld
t = tkinter.scrolledtext.ScrolledText(main,
            width=40, height=3)
t.pack()

# Inhalt der Datei anzeigen
bshow = tkinter.Button(main, text = "Anzeigen",
                       command = xshow)
bshow.pack()

bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


