import tkinter

def ende():
    main.destroy()

main = tkinter.Tk()

b1 = tkinter.Button(main, text="b1", command=ende)
b1.place(relx=0.5, rely=0, anchor="n")

b2 = tkinter.Button(main, text="b2", command=ende)
b2.place(relx=0, rely=0.25, anchor="w")

b3 = tkinter.Button(main, text="b3", command=ende)
b3.place(relx=0, rely=0.5, anchor="w")

b4 = tkinter.Button(main, text="b4", command=ende)
b4.place(relx=0, rely=0.75, anchor="w")

b5 = tkinter.Button(main, text="b5", command=ende)
b5.place(relx=0.5, rely=1, anchor="s")

main.mainloop()

