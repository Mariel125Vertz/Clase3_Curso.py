def factorial (n):
    if n==0: #caso base
        return 1
    else:
        return n* factorial(n-1)
factorial_30 = print(factorial(30))
     



def fibbonaci (n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbonaci (n-1)+ fibbonaci (n-1)
number=10
print (fibbonaci(number))

def naturales (n): 
     if n==0:
        return 0
     elif n==1:
        return 1
     else:
        return fibbonaci (n+1)
number=8
print (fibbonaci(number))