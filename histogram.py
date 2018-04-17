def histogram(array):
    """A histogram function"""
    for x in range (0,len(array)):
        print ('*' * array[x])
    return
array=[]
print("Enter range")
num=int(input())
for n in range(num):
    print("Enter the elements :")
    inp=int(input())
    array.append(inp)
print(array)
histogram(array)