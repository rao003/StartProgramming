lista = ["Alex","Bia","Catia", "error", "error"]

# add item
lista.insert(1,"Frank")
lista.append("Sara")

# change item
lista[2] = "Tom"

# remove item
lista.pop() # last item
lista.pop(2) # delete per index

#remove 
lista = ["Alex","Bia","Catia", "error", "error"]
lista.remove("error")
print(lista)

#replace

# TODO: 

#delete
del lista[1] # risk delete the entire list
del lista[1:4] # delete range
