adult = True
geld = True
visa = True 
login = True


if (login):
    if(adult):
        if (geld):
            if(visa):
                print("pode comprar")
            else:
                print("Precisa de cartao")        
        else:
            print("Ganhe dinheiro")
    else:
        print("precisa ter 18 anos")
else:
    print("Faca seu login")

if((login and geld) or (visa)):
    print ("pode comprar !!")
else:
    print("cai fora")