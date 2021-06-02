# ubung
"""
limit = int(input("enter the limit:"))

for x in range(1,limit+1):
    if (x%7 !=  0):
        print(x)
    else: 
        print("pass") 

"""
# ubung2

def check(x):
    if x%7 !=  0 :
        print(x)
    else: 
        print("pass")

def main():
    limit = int(input("enter the limit:"))

    for x in range(1,limit+1):
        check(x)

main()



