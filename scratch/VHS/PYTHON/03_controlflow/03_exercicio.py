adult = True
geld = True
visa = True
login = True


if (not login):
    print("login")
if (not adult):
    print("idade")
if (not visa):
    print ("cartao")
if (not geld):
    print ("grana")
if (login and adult and visa and geld == True):
    print ("compre !!!")


if ((not login) and (not adult) and (not visa) and (not geld)):
    print("Falta login e idade e cartao e grana")
elif ((not login) and (not adult) and (not visa) and (geld) ):
    print("Falta login e idade e cartao")
elif ((not login) and (not adult) and (visa) and (not geld)):
    print ("Falta login e idade e grana")
elif ((not login) and (adult) and (not visa) and (not geld)):
    print ("Falta login e cartao e grana")
elif ((login) and (not adult) and (not visa) and (not geld)):
    print("Falta idade e cartao  e grana")   
else: 
    print ("pode comprar")
