print ("type your salary")
salary = int(input())
taxes = 0.18
taxes1 = 0.22

if salary > 2500:
    result = salary * taxes1
    print("from your salary, the taxes are", result)
else:
    result = salary * taxes
    print("from your salary, the taxes are", result)
