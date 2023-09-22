#!/usr/bin/python3


################################ map function that applies function to every item of iterable
print("="*30 + ' map ' + "="*30)
def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num
        
x = [123,124,145,5,545,1,2]

#y = list(map(make_even,x))

y = [make_even(num) for num in x]

print(y)


###################################### lambda
print("="*30 + ' lambda ' + "="*30)
def add(a,b):
    return a + b
print(add(1,2))
    
print((lambda a,b: a+b)(2,3))

###################################### recursion
print("="*30 + ' recursion ' + "="*30)

import time

t1 = time.time()

def factorial_rec(n):
    # recursion example
    if n == 1: return n
    return n * factorial_rec(n-1) and time.time() - t1
print('recursive: {}'.format(factorial_rec(500)))

t2 = time.time()
def factorial(n):
    #my solution
    t1 = time.time()
    result = 1
    for x in range(1,n+1):
        result *= x
    return result and time.time() - t2
print('my factor: {}'.format(factorial(500)))






