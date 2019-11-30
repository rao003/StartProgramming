import tkinter

def ende():
    main.destroy()

main = tkinter.Tk()

# Schaltfläche Ende
b = tkinter.Button(main, text = "Ende", command = ende)
b.pack()

# Label, mit Bild
lb = tkinter.Label(main)
im = tkinter.PhotoImage(file="rheinwerk.png")
lb["image"] = im
lb.pack()

# Daten des Bildobjekts lesen
print("Breite:", im.width())
print("Höhe:", im.height())
print("Farbe x,y:", im.get(0, 0))
if not im.transparency_get(20, 20):
    print("Punkt ist nicht transparent")

# Daten des Bildobjekts ändern
for x in range(5, 94):
    for y in range(69, 80):
        im.put("#00549D", (x, y))
    for y in range(38, 46):
        im.transparency_set(x, y, True)

# Geänderte Daten des Bildobjekts lesen
if im.transparency_get(50, 40):
    print("Punkt ist transparent")

main.mainloop()


