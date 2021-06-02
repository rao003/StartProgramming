for x in range(10):
    print(x)


mList = ["mohamed", "ingo", "thomas"]
y = 0
for x in mList:
    y += 1
    print(str(y), "-"  , x.title())
    

print("amount of people", str(y))


z = 0
for x in range(10,100,10):
    z += 1
    print(x, "% [" , "#"*z , " "*(10-z), "]" )


for x in range(5):
    for y in range (100, 105):
        print (x, y) 

