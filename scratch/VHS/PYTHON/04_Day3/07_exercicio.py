

def gruess(*alunos):
    for x in alunos:
        print("Hallo DE", x)

def hello (*alunos):
    for y in alunos:
        print ("Hello EN", y)

user = int(input("enter 0 for DE and 1 for EN:"))

if user == 0:
    gruess("brasil", "alemanha", "dinamarca")
else:
    hello("brasil", "alemanha", "dinamarca")


