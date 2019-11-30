import tkinter.ttk

def ende():
    main.destroy()

def anzeigen():
    lb["text"] = "Zahl: " + spbZahl.get() \
        + ", Text: " + spbText.get()

main = tkinter.Tk()

lb = tkinter.Label(main,
    text = "Zahl: 12, Text: Stuttgart", width=25)
lb.pack()

spbZahl = tkinter.ttk.Spinbox(main,
    from_=10, to=15, width=15, command=anzeigen)
spbZahl.set(12)
spbZahl.pack()

spbText = tkinter.ttk.Spinbox(main,
    values=("Hamburg","Stuttgart","Berlin"),
    width=15, command=anzeigen)
spbText.set("Stuttgart")
spbText.pack()

bshow = tkinter.Button(main, text = "Anzeigen",
    command = anzeigen)
bshow.pack()

bende = tkinter.Button(main,
    text = "Ende", command = ende)
bende.pack()

main.mainloop()


