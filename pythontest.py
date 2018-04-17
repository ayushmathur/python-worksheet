pairs=[(4,"four"),(2,"Two"),(1,"one"),(5,"five")]
#pairs.sort()

pairs.sort(key=lambda x:x[1])
print(pairs)
x=[1,3,4,2,5]
y=list(map(lambda a: a+10,x))
print(y)

import functools
print(functools.reduce(lambda a,b: a if a<b else b , x))
z = x[:]
print(z)