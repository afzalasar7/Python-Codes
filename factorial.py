#using for loops
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*= i
    return f

#optimised code
from functools import reduce
def factorial1(n):
    return reduce(lambda x,y :x * y, [i for i in range(1,n+1)])


print(f"Factorial of number using for loops: {factorial(10)}")
print(f"Factorial of number with optimised function: {factorial1(10)}")