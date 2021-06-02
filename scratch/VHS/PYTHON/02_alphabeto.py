def nato(letra):
    for teste in natob:
        if teste.startswith(letra):
            print(letra + "" + teste)

natob = ["Alpha", "Beta", "Charlie"]
name = input("type your name")
for letra in name:
    nato(letra.upper())

