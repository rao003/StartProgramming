user = {"nome":"ricardo", "sobrenome":"oliveira", "plz":123}

listadeuser = {"nome":["maria", "ana", "joana"], "sobrenome":["silva", "souza", "santos"],"plz":[1,2,3]}


# add new key e de um valor
user["location"] = "hamburg"

# change o mesmo valor
user["location"] = "Kiel"

print(user)
print(listadeuser)

# outra possibilidde

listadeuser2 = [{"nome":"ricardo", "sobrenome":"oliveira", "plz":123}, {"nome":"maria"}, {"nome":"joana"}]

