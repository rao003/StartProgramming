import tkinter

def ende():
    main.destroy()

main = tkinter.Tk()

b1 = tkinter.Button(main, text="b1",
                    command=ende)
b1.place(x=50, y=50, anchor="se")

b2 = tkinter.Button(main, text="b2",
                    command=ende)
b2.place(x=50, y=50, anchor="sw")

b3 = tkinter.Button(main, text="b3",
                    command=ende)
b3.place(x=50, y=50, anchor="ne")

b4 = tkinter.Button(main, text="b4",
                    command=ende)
b4.place(x=50, y=50, anchor="nw")

main.mainloop()

