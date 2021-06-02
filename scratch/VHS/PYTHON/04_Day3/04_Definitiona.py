def greetings(name, teacher):
    print("Hallo", name)
    print("ok", teacher)

greetings("aluno", "ricardo")

def greetings2(id , name , plz, teacher):  
    print (id, name, plz, teacher)

greetings2 (name="Pessoa", id= 1, plz = 55555 , teacher= "professor")  # se definir pode alterar a sequencia, senao tem que entrar pela sequencia
greetings2 (1, "nome", 12345, "professor")

def greetings3 (id=0, name="aluno", plz=77777, teacher="diretor"): # se colocar o igual, se nao tiver nada no greeting, pega valor default
    print(id, name, plz, teacher)

greetings3()



