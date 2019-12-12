# Add your Python code here. E.g.
from microbit import *

y = 1
x = 1
z = 0

while z < 100:
    z = y + x 
    y = x
    x = z
    display.scroll(z)
    
    sleep(500)
