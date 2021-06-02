def leapyear(year):
    if (year % 4 == 0) or (year % 100 !=0) and (year % 400 ==0):
        print("leapyear")
    else:
        print("not")

leapyear(2000)
leapyear(2018)


