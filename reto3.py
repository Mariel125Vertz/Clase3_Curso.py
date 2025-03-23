def natu (n):
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  (n-0) + natu(n-1)
    


number=2
number1=2
while number1 > 0:
    for i in range(2):
        print(number1)
        number1 -= 1  
        break


     

print ("RESULTADO TOTAL: ",natu(number))

