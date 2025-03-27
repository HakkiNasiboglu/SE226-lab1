import math

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
answer = factorial(5)
print("Answer 1 =" , answer)

total = 0
def sin(x):
   global total





sm = 0
def function(n):
    global sm
    if n == 0:
        return
    else:
        function(n-1)
        sm = sm + 1 / n
function(5)
print("Answer 3 =" , sm)
