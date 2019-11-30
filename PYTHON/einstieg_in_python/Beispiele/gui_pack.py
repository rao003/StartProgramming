import tkinter

def ende():
    main.destroy()

main = tkinter.Tk()

# Frame 1 mit Schaltfläche 1a und 1b
fr1 = tkinter.Frame(main, width=200, height=100,
                    relief="sunken", bd=1)
fr1.pack(side="left")
b1a = tkinter.Button(fr1, text="Schaltfläche 1a")
b1a.pack(padx=5, pady=5)
b1b = tkinter.Button(fr1, text="Schaltfläche 1b")
b1b.pack(padx=5, pady=5)

# Frame 2 mit Schaltfläche 2a und 2b
fr2 = tkinter.Frame(main, width=200, height=100,
                    relief="sunken", bd=1)
fr2.pack(side="right")
b2a = tkinter.Button(fr2, text="Schaltfläche 2a")
b2a.pack(ipadx=25, ipady=25)
b2b = tkinter.Button(fr2, text="Schaltfläche 2b")
b2b.pack(fill="x")

# Frame 3
fr3 = tkinter.Frame(main, width=200, height=100,
                    relief="sunken", bd=1)
fr3.pack(side="bottom", expand=1, fill="both")

bende = tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()

