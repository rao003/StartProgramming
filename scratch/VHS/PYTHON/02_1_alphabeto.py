# definition 
def conversao(letra): # magica
    for teste in abc: # 
        if teste.startswith(letra): # seleciona a Inicial de cada letra do ABC
            print(letra + " = " + teste) # cada letra e sua ABC correspondente

# list of alphabet
abc = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee"]
name = input("type your name") # input do usuario

for letra in name: 
    conversao(letra.upper()) # converter para CAPS
