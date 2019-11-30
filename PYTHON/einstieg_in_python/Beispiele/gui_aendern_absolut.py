import tkinter

def ende():
    main.destroy()

# bewegt nach ganz links
def movetoleft():
    lb.place(relx=0, rely=0, anchor="nw")

# bewegt nach ganz rechts
def movetoright():
    lb.place(relx=1, rely=0, anchor="ne")

main = tkinter.Tk()

# Bewegtes Label
lb = tkinter.Label(main, text="Test",
                   relief="sunken", bd=1)
lb.place(relx=0, rely=0, anchor="nw")

# bewegt nach ganz links
bleft = tkinter.Button(main, text="ganz links",
                       command=movetoleft)
bleft.place(relx=0, rely=1, anchor="sw")

# bewegt nach ganz rechts
bright = tkinter.Button(main, text="ganz rechts",
                        command=movetoright)
bright.place(relx=1, rely=1, anchor="se")

bende = tkinter.Button(main, text="Ende",
                       command=ende)
bende.place(relx=0.5, rely=1, anchor="s")

main.mainloop()

