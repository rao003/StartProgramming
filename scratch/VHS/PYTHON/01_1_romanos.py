entry = int(input("digite seu numero"))
romano = ""
lista = ["I", "II", "III", "IV","V","VI","VII","VIII","IX"]

if entry < 30:                          # menor do que 30
    while(entry > 10):
        romano = romano + "X"
        entry = entry - 10
    romano = romano + lista[entry-1]
    print("seu numero", romano) 
elif entry in range (30,40):               # entre 31 e 40
    while(entry > 20):
        romano = romano + "X"
        entry = entry - 10
    while(entry > 10):
        romano = romano + "X"
        entry = entry - 10
    romano = romano + lista[entry-1]
    print("seu numero", romano) 
elif entry in range (40,50):              # entre 41 e 50
    while(entry > 10):
        
        entry = entry - 10
    romano = romano + lista[entry-1]
    print("seu numero","XL"+romano) 
elif entry in range (50,60):              # entre 51 e 60
    while(entry > 10):
        
        entry = entry - 10
    romano = romano + lista[entry-1]
    print("seu numero", "L"+romano)         
elif entry in range (60,90):              # entre 61 e 90
    entry = entry - 50
    while(entry > 20):
        romano = romano + "X"
        entry = entry - 10
    while(entry > 10):
        romano = romano + "X"
        entry = entry - 10
    romano = romano + lista[entry-1]
    print("seu numero","L"+ romano) 
elif entry in range (90,100):              # entre 91 e 99
    entry = entry - 90
    
    romano = romano + lista[entry-1]
    print("seu numero","XC"+ romano)
elif entry == 100:                         # 100 !!!!!!!!!!!!!!!!!!!! nicht optimiert ABER funktioniert Mohamed !!!
    print("C") 
else:
    print("too high")