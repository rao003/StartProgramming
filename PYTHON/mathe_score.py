import random
import time
import math
a = 0
b = 0
c = 0
score = 0
for x in range(10):
	a = random.randint(0,10)
	b = random.randint(0,10)
	print(a)
	print("x")
	print(b)
	c = int(input("What is the result?"))
	if c == a * b:
		score = score + 1
print("From 10 you got")
print(score)
print("correct")
# comment
