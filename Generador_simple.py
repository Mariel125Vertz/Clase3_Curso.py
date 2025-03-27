


#SERIE FIBONACCI 
def fibonacci (limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=a,b+2
for num in fibonacci (10):
    print (num )
    

