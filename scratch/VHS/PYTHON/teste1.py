visa = False
age = False
geld = False
login = True


if (not visa):
    print ("Erro1: falta cartao")
if (not age):
    print ("Erro2: falta idade")
if (not geld):
    print ("Erro3: falta geld")
if (not login):
    print ("Erro4: falta login")
if (visa and age and geld and login):
    print ("voce pode comprar")


