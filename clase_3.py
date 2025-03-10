import numpy as np
prices=np.array([100,200,300])
discount=np.array([0.9])
discount_price=prices*discount
print(discount_price)


prices=np.random.randint(100,500, size=(3,3))
discount=np.array([10,20,30])
resultado= prices+ discount
print(prices)
print(resultado)

array=np.array([1,2,3,4,5])
print(np.any(array>4))

array_a=np.array([1,2,3])
array_b=np.array([4,5,6])
concatenated=np.concatenate((array_a, array_b))
print(concatenated)


array_a=np.array([1,2,3])
array_b=np.array([4,5,6])
satecked_v=np.vstack((array_a,array_b))  
print (satecked_v)


satecked_h=np.hstack((array_a,array_b))  
print (satecked_h)


#division de array 
array_c=np.arange(1,10)
split_array=np.split(array_c,3)
print(array_c)
print(split_array)