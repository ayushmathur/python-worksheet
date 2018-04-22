import numpy as np 
a=np.array([1,2,3,4])
b=np.array([4,5,6,7])
print(a*b)
print(a+3)

arr=np.arange(24).reshape(8,3)
print("Array : ")
print(arr)
print("Dimension: ",arr.ndim)
print("Dimension: ",arr.size)