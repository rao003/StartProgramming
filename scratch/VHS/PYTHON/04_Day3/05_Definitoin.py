def area (x,y):
    print(x*y)

area (5,6)

def area2 (x,y):
    name = "ricardo"
    name += "oliveira"
    result = x * y
    return result, name

myarea, nomecompleto = area2(5,6)

print ("a area é:", myarea, nomecompleto)


def pythonCourse (*alunos):
    for x in alunos:
        print(x)



def pythonCourse (*alunos):
    for x in alunos:
        if(x== "ricardo"):
            print("ricardo é lindo")
        else:    
            print(x)

pythonCourse ("ricardo")
pythonCourse ("teste", "ricardo")

